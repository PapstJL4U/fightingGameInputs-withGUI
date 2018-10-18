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

        #Labels
        notLabel = QLabel("<h1>Combo</h1>")
        listLabel = QLabel("<h2>List of notations</h2>")
        imgLabel = QLabel("<h2>Notation preview</h2>")

        #Edit field font
        notationFont = QFont()
        notationFont.setPointSize(20)
        #Edit field
        self.notEdit = QLineEdit()
        self.notEdit.setPlaceholderText("2 mp , 4 mp > hp qcb mk srk 2p" )
        self.notEdit.setMinimumHeight(50)
        self.notEdit.setFont(notationFont)
        self.notEdit.textChanged[str].connect(self.onChanged)

        #List field for Notation
        self.notList = QListWidget()
        #self.notList.itemPressed.connect(self.listItemPressed)
        self.notList.itemPressed.connect(self.itemPressed)
        self.notList.setToolTip('Select a combo and press "DEL" to delete it.')

        #buttons
        expNotationB = QPushButton("Export single notation")
        expNotationB.clicked.connect(self.expNotation)
        addNotationB = QPushButton("Add notation to list")
        addNotationB.clicked.connect(self.addNotation)
        expListB = QPushButton("Export list")
        expListB.clicked.connect(self.expList)
        clearListB =  QPushButton("Clear list")
        clearListB.clicked.connect(self.clearList)

        #notation image
        self.notImage = QPixmap('assets'+sep+'default.png')
        self.pxlbl = QLabel(self)
        self.pxlbl.setPixmap(self.notImage)
        self.imageArea =  QScrollArea()
        self.imageArea.setWidget(self.pxlbl)
        self.imageArea.setMaximumHeight(150)

        print(str(self.imageArea.size())+"in init")

        #group for the layout

        #Layout for the input and image
        vboxleft = QVBoxLayout()
        topleft = QGroupBox(self)

        vboxleft.addWidget(notLabel)
        vboxleft.addWidget(self.notEdit)
        vboxleft.addWidget(imgLabel)
        vboxleft.addWidget(self.imageArea)

        topleft.setLayout(vboxleft)

        #Layout for the list of notations
        vboxright = QVBoxLayout()
        topright = QGroupBox(self)
        vboxright.addWidget(listLabel)
        vboxright.addWidget(self.notList)
        topright.setLayout(vboxright)

        #layout for the buttons
        gridboxbottom = QGridLayout()
        bottom = QGroupBox(self)
        gridboxbottom.addWidget(expNotationB, 0, 0)
        gridboxbottom.addWidget(addNotationB, 0, 1)
        gridboxbottom.addWidget(expListB, 0, 2)
        gridboxbottom.addWidget(clearListB, 0, 3)
        bottom.setLayout(gridboxbottom)

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)
        #add components

        grid.addWidget(splitter2)
        self.setLayout(grid)
        self.setGeometry(400, 400, 500, 250)
        self.setWindowTitle("Combo Notation Image Maker")
        self.centerUI()
        self.show()

    def centerUI(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def addNotation(self):

        if self.notEdit.text() != "":
            self.notList.addItem(self.notEdit.text())
            print("added notation to list")

    def expNotation(self):
        color = ['-c','0 0 0 0']
        game = ['-g','sf']
        outputfile = ['-o', self.notEdit.text()]
        inputstring = ['-i', self.notEdit.text()]
        inputparser(game+inputstring+outputfile+color)
        print("exported notation image")

    def expList(self):
        #TODO parse all Combos from list one by one
        print("exported complete list")

    def clearList(self):
        self.notList.clear()

    def keyPressEvent(self, QKeyEvent):

        if QKeyEvent.key() == Qt.Key_Enter or QKeyEvent.key() == Qt.Key_Return:
            self.addNotation()
            self.notEdit.clear()

        if QKeyEvent.key() == Qt.Key_Delete and self.notList.hasFocus() and self.notList.count() > 0:
            item = self.notList.selectedItems()[0]
            row=self.notList.row(item)
            self.notList.takeItem(row)


    def onChanged(self, text):
        color = ['-c','0 0 0 0']
        game = ['-g','sf']
        outputfile = ['-o', 'temp']
        inputstring = ['-i', text]
        inputparser(game+inputstring+outputfile+color)
        self.renewImage()

    def itemPressed(self):
        try:
            if self.notList.count() > 0:
                item = self.notList.selectedItems()[0]
                #parseCombo(item.text(), "temp", "0 0 0 0")
                self.renewImage()
                print("preview combo image..."+item.text())
        except:
            raise

    def renewImage(self):
        self.notImage.load("output"+sep+"temp.png")
        self.pxlbl.setPixmap(self.notImage)
        self.pxlbl.setMinimumSize(self.notImage.size())

if __name__ == '__main__':

    app = QApplication(sys.argv)
    cApp = ComboApp()
    cApp.setMinimumSize(1000, 500)
    sys.exit(app.exec_())

