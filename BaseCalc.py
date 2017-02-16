 # Jeremy Bouchard
 # Emile Belanger
 # 2016/02/15
 # Pour executer, utiliser la commande : python BaseCalc.py

from tkinter import *
from tkinter.messagebox import *

class GUI:
    current = 0
    last = 0
    power = 0
    dot = 0
    negative = 0
    temp = 0
    lastOperation = ""
    history = ""

    def __init__(self, master):
        self.master = master

        master.title("BaseCalc")
        master.geometry("400x600")
        master.resizable(width  = False, height = False)
        master.config(background = "black")

        menubar = Menu(master)

        menu1 = Menu(menubar, tearoff = 0)
        menu1.add_command(label = "Historique", command = self.showHistory)
        menu1.add_command(label = "Effacer l'historique",
            command = self.clearHistory)
        menu1.add_command(label = "Imprimer", command = self.printHistory)
        menu1.add_separator()
        menu1.add_command(label = "Quitter", command = master.quit)
        menubar.add_cascade(label = "Option", menu = menu1)

        menu2 = Menu(menubar, tearoff = 0)
        menu2.add_command(label = "Obtenir de l'aide", command = self.getHelp)
        menu2.add_separator()
        menu2.add_command(label = "À propos", command = self.getAbout)
        menubar.add_cascade(label = "Aide", menu = menu2)

        master.config(menu = menubar)

        self.display = Canvas(master, bg = "black", width = 400, height = 100,
            highlightthickness = 0)
        self.text = self.display.create_text(390, 52, fill = "white",
            anchor = "e", font = "Helvetica -40")
        self.display.grid(row = 0, column = 0, columnspan = 4, rowspan = 2)

        buttonC = Button(master, height = 3, text = "C",
            font = "Helvetica -24", bg = "grey",
            command = lambda : self.getClicked("C"))
        buttonC.grid(column = 0, row = 2, sticky=W+E+N+S)

        buttonDiv = Button(master, height = 3, text = "/",
            font = "Helvetica -24", bg = "grey",
            command = lambda : self.getClicked("/"))
        buttonDiv.grid(column = 1, row = 2, sticky=W+E+N+S)

        buttonMul = Button(master, height = 3, text = "*",
            font = "Helvetica -24", bg = "grey",
            command = lambda : self.getClicked("*"))
        buttonMul.grid(column = 2, row = 2, sticky=W+E+N+S)

        buttonSub = Button(master, height = 3, text = "-",
            font = "Helvetica -24", bg = "chocolate1",
            command = lambda : self.getClicked("-"))
        buttonSub.grid(column = 3, row = 2, sticky=W+E+N+S)

        button7 = Button(master, height = 3, text = "7",
            font = "Helvetica -24", bg = "grey",
            command = lambda : self.getClicked("7"))
        button7.grid(column = 0, row = 3, sticky=W+E+N+S)

        button8 = Button(master, height = 3, text = "8",
            font = "Helvetica -24", bg = "grey",
            command = lambda : self.getClicked("8"))
        button8.grid(column = 1, row = 3, sticky=W+E+N+S)

        button9 = Button(master, height = 3, text = "9",
            font = "Helvetica -24", bg = "grey",
            command = lambda : self.getClicked("9"))
        button9.grid(column = 2, row = 3, sticky=W+E+N+S)

        button4 = Button(master, height = 3, text = "4",
            font = "Helvetica -24", bg = "grey",
            command = lambda : self.getClicked("4"))
        button4.grid(column = 0, row = 4, sticky=W+E+N+S)

        button5 = Button(master, height = 3, text = "5",
            font = "Helvetica -24", bg = "grey",
            command = lambda : self.getClicked("5"))
        button5.grid(column = 1, row = 4, sticky=W+E+N+S)

        button6 = Button(master, height = 3, text = "6",
            font = "Helvetica -24", bg = "grey",
            command = lambda : self.getClicked("6"))
        button6.grid(column = 2, row = 4, sticky=W+E+N+S)

        buttonAdd = Button(master, height = 3, text = "+",
            font = "Helvetica -24", bg = "chocolate1",
            command = lambda : self.getClicked("+"))
        buttonAdd.grid(column = 3, row = 3, rowspan = 2, sticky=W+E+N+S)

        button1 = Button(master, height = 3, text = "1",
            font = "Helvetica -24", bg = "grey",
            command = lambda : self.getClicked("1"))
        button1.grid(column = 0, row = 5, sticky=W+E+N+S)

        button2 = Button(master, height = 3, text = "2",
            font = "Helvetica -24", bg = "grey",
            command = lambda : self.getClicked("2"))
        button2.grid(column = 1, row = 5, sticky=W+E+N+S)

        button3 = Button(master, height = 3, text = "3",
            font = "Helvetica -24", bg = "grey",
            command = lambda : self.getClicked("3"))
        button3.grid(column = 2, row = 5, sticky=W+E+N+S)

        button0 = Button(master, height = 3, text = "0",
            font = "Helvetica -24", bg = "grey",
            command = lambda : self.getClicked("0"))
        button0.grid(column = 0, row = 6, columnspan = 2, sticky=W+E+N+S)

        buttonDot = Button(master, height = 3, text = ".",
            font = "Helvetica -24", bg = "grey",
            command = lambda : self.getClicked("."))
        buttonDot.grid(column = 2, row = 6, sticky=W+E+N+S)

        buttonEq = Button(master, height = 3, text = "=",
            font = "Helvetica -24", bg = "chocolate1",
            command = lambda : self.getClicked("="))
        buttonEq.grid(column = 3, row = 5, rowspan = 2, sticky=W+E+N+S)

        master.bind("<Key>", self.getKeyboard)

    def showHistory(self):
        showinfo("Historique", "Historique des calculs\n"+
        self.history)

    def printHistory(self):
        showinfo("Impression", "Impression en cours")

    def getHelp(self):
        showinfo("Aide", "L'aide va ici")

    def clearHistory(self):
        showinfo("Historique", "Effacement en cours")

    def getAbout(self):
        showinfo("À propos de ce logiciel", "BaseCalc v1.0.3\n"+
            "Copyright © 2017 Jérémy Bouchard & Émile Bélanger\n\n")

    def getClicked(self, pressed):
        if not (pressed == "="):
            self.history += pressed
            if (pressed == "C" or pressed == "c"):
                self.history += "\n"
        self.addToEquation(pressed)

    def getKeyboard(self, event):
        if (event.char == "1" or event.char == "2" or event.char == "3"
        or event.char == "4" or event.char == "5" or event.char == "6"
        or event.char == "7" or event.char == "8" or event.char == "9"
        or event.char == "-" or event.char == "+" or event.char == "="
        or event.char == "/" or event.char == "*" or event.char == "C"
        or event.char == "0" or event.char == "." or event.char == "c"):
            if not (event.char == "="):
                self.history += event.char
                if (event.char == "C" or event.char == "c"):
                    self.history += "\n"
            self.addToEquation(event.char)

    def doOperation(self, key):
        if (key == "+"):
            self.last = self.current
            self.resetCurrent()
            self.lastOperation = "+"
        if (key == "-"):
            self.last = self.current
            self.resetCurrent()
            self.lastOperation = "-"
        if (key == "*"):
            self.last = self.current
            self.resetCurrent()
            self.lastOperation = "*"
        if (key == "/"):
            self.last = self.current
            self.resetCurrent()
            self.lastOperation = "/"
        if (key == "="):
            if (self.lastOperation == "+"):
                if (isinstance(self.last, float) or
                isinstance(self.current, float) or
                isinstance(self.current, str) or
                isinstance(self.last, str)):
                    self.current = float(self.current) + float(self.last)
                else:
                    self.current = int(self.current) + int(self.last)
                self.history += key
                self.history += str(self.current)
                self.history += "\n"
                self.negative = 0
                self.lastOperation = ""
            if (self.lastOperation == "-"):
                if (isinstance(self.last, float) or
                isinstance(self.current, float) or
                isinstance(self.current, str) or
                isinstance(self.last, str)):
                    self.current = float(self.last) - float(self.current)
                else:
                    self.current = int(self.last) - int(self.current)
                self.history += key
                self.history += str(self.current)
                self.history += "\n"
                self.lastOperation = ""
                self.negative = 0
            if (self.lastOperation == "*"):
                if (isinstance(self.last, float) or
                isinstance(self.current, float) or
                isinstance(self.current, str) or
                isinstance(self.last, str)):
                    self.current = float(self.current) * float(self.last)
                else:
                    self.current = int(self.current) * int(self.last)
                self.history += key
                self.history += str(self.current)
                self.history += "\n"
                self.negative = 0
                self.lastOperation = ""
            if (self.lastOperation == "/"):
                if (isinstance(self.last, float) or
                isinstance(self.current, float) or
                isinstance(self.current, str) or
                isinstance(self.last, str)):
                    self.current = float(self.last) / float(self.current)
                else:
                    self.current = int(self.last) / int(self.current)
                self.history += key
                self.history += str(self.current)
                self.history += "\n"
                self.negative = 0
                self.lastOperation = ""

    def addToEquation(self, key):
        if not (key == "-" or key == "+" or key == "=" or key == "/"
        or key == "*" or key == "C" or key == "c"):
        # To create the number

            if (key != "." or (key == "." and self.dot == 0)):
                if (len(str(self.current)) < 17):
                    if (self.current == 0 and key != "."):
                        if (key == "0"):
                            self.current = int(0)
                        else:
                            self.current = int(key)
        # To add digits correctly with decimal dot
                    else:
                        self.current = str(self.current) + key
                        if (isinstance(self.current, int)):
                            self.current = int(self.current)
                        if (isinstance(self.current, float)):
                            self.current = float(self.current)
        # Add the digits but keep to data float or int

        if (key == "c" or key == "C"):
            self.resetCurrent()
        # Clear the data

        if (key == "."):
            self.dot = 1

        if (key == "-" and self.current == 0):
            if (self.negative == 0):
                self.negative = 1
            else:
                self.negative = 0
        # Change to negative value if starts with 0

        if (self.negative == 1 and float(self.current) > 0):
            if (isinstance(self.current, int)):
                self.current = 0 - int(self.current)
            else:
                self.current = 0 - float(self.current)
        # Change to negative if actually negative

        if ((key == "-" and self.current != 0) or key == "+"
        or key == "=" or key == "/" or key == "*"):
            self.doOperation(key)

    def resetCurrent(self):
        self.current = 0
        self.dot = 0
        self.negative = 0
        self.temp = 0
        self.lastOperation = 0

    def showNumber(self):
        self.display.itemconfig(self.text, text = self.current)
        root.after(100, self.showNumber)

if __name__ == "__main__":

    root = Tk()
    gui = GUI(root)
    gui.showNumber()
    root.mainloop()
