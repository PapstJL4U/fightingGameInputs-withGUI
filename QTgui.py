#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from inputs_tti import main as inputparser
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from os import sep


class ComboApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        grid = QGridLayout()

        # Labels
        notLabel = QLabel("<h1>Combo</h1>")
        listLabel = QLabel("<h2>List of notations</h2>")
        imgLabel = QLabel("<h2>Notation preview</h2>")

        # Edit field font
        notationFont = QFont()
        notationFont.setPointSize(20)

        # Edit field
        self.notEdit = QLineEdit()
        self.notEdit.setPlaceholderText("2 mp , 4 mp > hp qcb mk srk 2p")
        self.notEdit.setMinimumHeight(50)
        self.notEdit.setFont(notationFont)
        self.notEdit.setDragEnabled(True)
        self.notEdit.setToolTip('You need to place a space between each command. Like "2 lp xx 623 HP')
        self.notEdit.textChanged[str].connect(self.onChanged)
        self.notEdit.selectionChanged.connect(self.renewImage)

        # List field for Notation
        self.notList = QListWidget()
        #self.notList.itemPressed.connect(self.listItemPressed)
        self.notList.itemPressed.connect(self.itemPressed)
        self.notList.setToolTip('Select a combo and press "DEL" to delete it.')

        # buttons
        expNotationB = QPushButton("Export combo notation")
        expNotationB.clicked.connect(self.expNotation)
        addNotationB = QPushButton("Add notation to list")
        addNotationB.clicked.connect(self.addNotation)
        expListB = QPushButton("Export list")
        expListB.clicked.connect(self.expList)
        clearListB =  QPushButton("Clear list")
        clearListB.clicked.connect(self.clearList)
        self.comboBox = QComboBox(self)
        self.comboBox.addItems(["sf", "dbfz", "ggxrd", "ggxrd_modern", "bbcrosstag"])
        self.comboBox.activated[str].connect(self.updateGame)

        # notation image
        self.notImage = QPixmap('assets'+sep+'default.png')
        self.pxlbl = QLabel(self)
        self.pxlbl.setPixmap(self.notImage)
        self.imageArea =  QScrollArea()
        self.imageArea.setWidget(self.pxlbl)
        self.imageArea.setMaximumHeight(150)

        #print(str(self.imageArea.size())+"in init")

        # group for the layout

        # Layout for the input and image
        vboxleft = QVBoxLayout()
        topleft = QGroupBox(self)

        vboxleft.addWidget(notLabel)
        vboxleft.addWidget(self.notEdit)
        vboxleft.addWidget(imgLabel)
        vboxleft.addWidget(self.imageArea)

        topleft.setLayout(vboxleft)

        # Layout for the list of notations
        vboxright = QVBoxLayout()
        topright = QGroupBox(self)
        vboxright.addWidget(listLabel)
        vboxright.addWidget(self.notList)
        topright.setLayout(vboxright)

        # layout for the buttons
        gridboxbottom = QGridLayout()
        bottom = QGroupBox(self)
        gridboxbottom.addWidget(expNotationB, 0, 0)
        gridboxbottom.addWidget(addNotationB, 0, 1)
        gridboxbottom.addWidget(expListB, 0, 2)
        gridboxbottom.addWidget(clearListB, 0, 3)
        gridboxbottom.addWidget(self.comboBox, 0, 4)
        bottom.setLayout(gridboxbottom)

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        # add components
        grid.addWidget(splitter2)
        self.setLayout(grid)
        self.setGeometry(400, 400, 500, 250)
        self.setWindowTitle("Combo Notation Image Maker")
        self.centerUI()
        self.show()

        # default variables
        self.game = ['-g', "sf"]
        self.colour = ['-c', "0 0 0 0"]

    def centerUI(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def addNotation(self):
        if not self.notEdit.text().isspace():
            self.notList.addItem(self.notEdit.text().lstrip().rstrip())

    def expNotation(self):
        color = self.colour
        game = self.game
        outputfile = ['-o', self.notEdit.text()]
        inputstring = ['-i', self.notEdit.text()]
        inputparser(game+inputstring+outputfile+color)

    def expList(self):
        color = self.colour
        game = self.game
        for i in range(0, self.notList.count()):
            inputstring = ['-i', self.notList.item(i).text()]
            outputfile = inputstring
            inputparser(game+inputstring+outputfile+color)

    def clearList(self):
        self.notList.clear()

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Enter or QKeyEvent.key() == Qt.Key_Return:
            if not self.notEdit.text().isspace():
                self.addNotation()
            self.notEdit.clear()
            self.onChanged(self.notEdit.placeholderText())

        if QKeyEvent.key() == Qt.Key_Delete and self.notList.hasFocus() and self.notList.count() > 0:
            item = self.notList.selectedItems()[0]
            row = self.notList.row(item)
            self.notList.takeItem(row)

    def onChanged(self, text):
        if len(text) > 0 and not text.isspace():
            color = self.colour
            game = self.game
            outputfile = ['-o', 'temp']
            inputstring = ['-i', text.lstrip(" ").rstrip(" ")]
            inputparser(game + inputstring + outputfile + color)
            self.renewImage()

    def itemPressed(self):
        try:
            if self.notList.count() > 0:
                item = self.notList.selectedItems()[0]
                color = self.colour
                game = self.game
                outputfile = ['-o', 'temp']
                inputstring = ['-i', item.text().lstrip(" ").rstrip(" ")]
                inputparser(game + inputstring + outputfile + color)
                self.renewImage()
        except:
            raise

    def renewImage(self, image = "temp"):
        img = image
        try:
            if img == "temp":
                self.notImage.load("output"+sep+img+".png")
            else:
                self.notImage.load("assets"+sep+img+".png")
            self.pxlbl.setPixmap(self.notImage)
            self.pxlbl.setMinimumSize(self.notImage.size())
        except:
            raise

    def updateGameColour(self, game = "sf", colour = "0 0 0 0"):
        self.game = ['-g', game]
        self.colour = ['-c', colour]

    def updateGame(self, text):
        self.game = ['-g', text]
        self.onChanged(self.notEdit.text())

    def updateColour(self):
        #TODO
        print("TODO")
        self.colour = ['-c', "TODO"]

if __name__ == '__main__':

    app = QApplication(sys.argv)
    cApp = ComboApp()
    cApp.setMinimumSize(1000, 500)
    sys.exit(app.exec_())