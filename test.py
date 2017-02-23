from BaseCalc import *

if __name__ == "__main__":

    root = Tk()
    import doctest
    doctest.testfile('BaseCalc.py', extraglobs={'gui':GUI(root)})
