from BaseCalc import *
import doctest

if __name__ == "__main__":

    root = Tk()
    doctest.testfile('BaseCalc.py', extraglobs={'gui':GUI(root)})
