#!/usr/bin/python
from tkinter import *
from tkinter.ttk import *
""""
root = Tk()
root.title("Combo Notation")
top=root.winfo_toplevel()
root.columnconfigure(0, weight=2)
root.rowconfigure(0, weight=1)
root.minsize(500, 250)
root.maxsize(1500,750)
"""
class App(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid(sticky=N+S+E+W)
        self.createWidgets()

    def createWidgets(self):
        top=self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.createLayout(self)

    def createLayout(self, master):
        self.bframe = Frame(self, relief=GROOVE, padding='5p')
        self.bframe.grid(row=1, columnspan=6, sticky=S)
        self.bframe.columnconfigure(250,weight=1)
        self.bframe.rowconfigure(50,weight=1)
        #self.bframe.
        #Button configuration
        exportNotation = Button(self.bframe, text="Export Combo Image", command=self.exportNotation)
        exportNotation.grid(row=0, column=0, sticky=(N, W, E, S))
        addNotationToList = Button(self.bframe, text="Add notation to the list", command=self.addNotation)
        addNotationToList.grid(row=0, column=1, sticky=(N, W, E, S))
        exportList = Button(self.bframe, text="Export List", command=self.exportList)
        exportList.grid(row=0, column=2, sticky=(N, W, E, S))

        #frame, that contains Notation input, notation display and image displa
        self.nframe = Frame(self, relief=GROOVE, padding='5p')
        self.nframe.grid(row=0, column=0, sticky=N+S+E+W)
        self.nframe.columnconfigure(20,weight=1)
        self.nframe.rowconfigure(125,weight=1)
        #Textfield
        self.notationEntry = Entry(self.nframe)
        self.notationEntry.delete(0,END)
        self.notationEntry.insert(0, "2 mp , 4 mp > hp qcb mk srk 2p")
        self.notationEntry.focus_set()

        self.notationLabel = Label(self.nframe, text="Enter the notation here:")
        self.notationScrollbar = Scrollbar(self.nframe, orient=HORIZONTAL, command=self.notationEntry.xview)
        self.notationEntry.config(xscrollcommand=self.notationScrollbar.set)


        #Image display and image scrolling
        self.iframe = Frame(self.nframe)
        self.imageLabel = Label(self.iframe, text="Notation image:")
        self.iframescrollbar = Scrollbar(self.iframe, orient=HORIZONTAL)

        self.imageCanvas = Canvas(self.iframe, width=200, height=100)
        self.imageCanvas.config(xscrollcommand=self.iframescrollbar.set)
        self.iframescrollbar.config( command=self.imageCanvas.xview)


        self.notationLabel.grid(row=0, column=0, sticky=N+S+E+W)
        self.notationEntry.grid(row=1, column=0, sticky=N+S+E+W)
        self.notationScrollbar.grid(row=2, column=0, sticky=N+S+E+W)
        self.imageLabel.grid(row=3, column=0)
        self.iframe.grid(row=4, column=0, sticky=N+S+E+W)
        self.imageCanvas.grid(row=5, column=0)
        self.iframescrollbar.grid(row=6, column=0, sticky=N+S+E+W)


        self.imageCanvas.create_rectangle(0, 0, 200, 100, fill="blue")

        #frame, that contains the list of notations
        lframe = Frame(self, relief=GROOVE, padding='5p')
        lframe.grid(row=0, column=1, sticky=(N, W, E, S))
        lframe.columnconfigure(250,weight=1)
        lframe.rowconfigure(250,weight=1)
        self.listLabel = Label(lframe, text="List of notations:")

        self.listbox = Listbox(lframe)
        for item in ["one", "two", "three", "four"]:
            self.listbox.insert(END, item)

        xscrollbar = Scrollbar(lframe, orient=HORIZONTAL)
        xscrollbar.config(command=self.listbox.xview)
        self.listbox.config(xscrollcommand=xscrollbar.set)
        yscrollbar = Scrollbar(lframe)
        self.listbox.config(yscrollcommand=yscrollbar.set)
        yscrollbar.config(command=self.listbox.yview)

        self.listLabel.grid(row=0, column=0, sticky=(N, W, E, S))
        self.listbox.grid(row=1, column=0, sticky=(N, S))
        self.listbox.rowconfigure(100, weight=1)
        xscrollbar.grid(row=2, column=0, sticky=(N, W, E, S))
        yscrollbar.grid(row=1, column=1, sticky=(N, W, E, S))


    def exportNotation(self):
        print("exportNotation")

    def addNotation(self):
        print("addNotation method")
        input = self.notationEntry.get()
        self.listbox.insert(END, input)

    def exportList(self):
        print("exportList")

#app = App(root)
#root.mainloop()
app=App()
app.master.title("Combo Notation")
app.mainloop()