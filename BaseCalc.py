 # Jeremy Bouchard
 # Emile Belanger
 # 2016/02/22
 # Pour executer, utiliser la commande : python BaseCalc.py

from tkinter import *
from tkinter.messagebox import *

class GUI:
    unit = 0
    decimal = 0
    current = 0
    last = 0
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

        self.current = round(float(self.current), 2)
        self.last = round(float(self.last), 2)
        self.temp  = round(float(self.temp), 2)

    def showHistory(self):
        showinfo("Historique", "Historique des calculs\n" + self.history)
        return 0

    def printHistory(self):
        showinfo("Impression", "L'historique suivant sera imprimé :\n"+
        self.history)
        return 0

    def getHelp(self):
        showinfo("Aide", "Utilisation de la calculatrice :\n\n\n"+
            "1- L'entrée peut se faire au clavier ou avec la souris\n\n"+
            "2- Pour afficher le résultat, appuyer sur '='\n\n"+
            "3- Pour effacer le calcul en cours, appuyer sur 'c'\n\n"+
            "4- Il est possible de  poursuivre un calcul deja en cours\n"+
            "    après l'ajout d'un opérateur, l'opérateur est alors\n"+
            "    ajouté au dernier résultat.\n\n"+
            "5- Pour calculer avec un nombre négatif, appuyer sur '-'\n"+
            "    avant le nombre, par exemple 3+-4=-1 et -0.5+1=0.5\n\n"+
            "6- Affichage de l'historique : Option->Historique\n\n"+
            "7- Suppression de l'historique : Option->Effacer l'historique\n\n"+
            "8- Impression de l'historique : Option->Imprimer\n\n")
        return 0

    def clearHistory(self):
        showinfo("Historique", "Historique effacé")
        self.history = ""
        return 0

    def getAbout(self):
        showinfo("À propos de ce logiciel", "BaseCalc\n"+
            "Copyright © 2017 Jérémy Bouchard & Émile Bélanger\n\n")
        return 0

    def getClicked(self, pressed):
        if not (pressed == "="):
            self.history += pressed #Add the key pressed to history
            if (pressed == "C" or pressed == "c"):
                self.history += "\n" #Switch line in history
        self.doCalculation(pressed) #Go do the real stuff
        return 0

    def getKeyboard(self, event):
        if (event.char == "1" or event.char == "2" or event.char == "3"
        or event.char == "4" or event.char == "5" or event.char == "6"
        or event.char == "7" or event.char == "8" or event.char == "9"
        or event.char == "-" or event.char == "+" or event.char == "="
        or event.char == "/" or event.char == "*" or event.char == "C"
        or event.char == "0" or event.char == "." or event.char == "c"):
            self.getClicked(event.char) #Pass the keyboard entry to the rest
        return 0

    def concatenateCurrent(self, key):
        if (key != "." or (key == "." and self.dot == 0)): #Dot "mutex"
            if (len(str(self.current)) < 17): #Max lenght printable
                if (self.current == 0 and key != "."):
                    if (key == "0"): #If there's nothing in the current
                        self.unit = float(0)
                    else:
                        self.unit = int(key)
                elif (key == "."): #Set the dot "mutex" to yes
                    self.dot = 1
                else:
                    if (self.dot == 0): #Do stuff related to unit
                        self.unit = str(self.unit) + str(key)
                    elif (self.decimal == 0): #Do suff related to decimal
                        self.decimal = str(key)
                    else:
                        self.decimal = str(self.decimal) + str(key)
                value = str(self.unit) + "." + str(self.decimal) #concatenate
        return float(value)

    def resolveNegative(self):
        if (self.current == 0): #Change negative "mutex"
            if (self.negative == 0):
                self.negative = 1
            else:
                self.negative = 0

        if (float(self.current) > 0): #Invert the number
            self.current = 0 - self.current

    def add(self, a, b):
        return float(a) + float(b)

    def sub(self, a, b):
        return float(b) - float(a)

    def mul(self, a, b):
        return float(a) * float(b)

    def div(self, a, b):
        return float(b) / float(a)

    def doCalculation(self, key):
        if not (key == "-" or key == "+" or key == "=" or key == "/"
        or key == "*" or key == "C" or key == "c"):
            self.current = self.concatenateCurrent(key)

        if (key == "c" or key == "C"):
            self.resetCurrent()

        if (key == "-" or self.negative == 1):
            self.resolveNegative()

        if ((key == "-" and self.current != 0) or key == "+"
        or key == "=" or key == "/" or key == "*"):
            if (key == "+" or key == "-" or key == "*" or key == "/"):
                self.last = self.current
                self.resetCurrent()
                self.lastOperation = key

            if (key == "="):
                if (self.lastOperation == "+"):
                    self.current = self.add(self.current, self.last)

                if (self.lastOperation == "-"):
                    self.current = self.sub(self.current, self.last)

                if (self.lastOperation == "*"):
                    self.current = self.mul(self.current, self.last)

                if (self.lastOperation == "/"):
                    self.current = self.div(self.current, self.last)

                self.history += key
                self.history += str(self.current)
                self.history += "\n"
                self.negative = 0
                self.lastOperation = ""

    def resetCurrent(self):
        self.current = float(0)
        self.dot = 0
        self.negative = 0
        self.temp = float(0)
        self.lastOperation = 0
        self.unit = 0
        self.decimal = 0
        return 0

    def showNumber(self):
        self.current = round(self.current, 2)
        self.display.itemconfig(self.text, text = self.current)
        root.after(100, self.showNumber)
        return 0

if __name__ == "__main__":

    root = Tk()
    gui = GUI(root)
    gui.showNumber()
    root.mainloop()
