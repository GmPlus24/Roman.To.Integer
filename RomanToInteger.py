from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import sys
import ctypes

from RomanToIntegerUI import Ui_MainWindow

class RomanToInteger(QMainWindow, Ui_MainWindow):
    def __init__(self , appXX ):
        super().__init__()
        self.app = appXX
        
        self.conversion = {
            "I":    1,
            "V":     5,
            "X":     10,
            "L":    50,
            "C":     100,
            "D":     500,
            "M":    1000,
            "IV":     4,
            "IX":     9,
            "XL":     40,    "XC":90,
            "CD":     400,   "CM":900
        
        }
        
        
        self.setupUi(self)
        self.setWindowIcon(QIcon("RomanToInteger-icon.png"))
        
        
        # setup UI
        self.label1.setFont(QFont("Sanserif", 13, QFont.Weight.Bold))
        self.buttonBackspace.setText("")
        self.buttonCopyRoman.setText("")
        self.buttonCopyInteger.setText("")
        self.buttonBackspace.setIcon(QIcon("Backspace-icon.png"))
        self.buttonBackspace.setIconSize(QSize(20,20))
        self.buttonCopyRoman.setIcon(QIcon("copy-icon.png"))
        self.buttonCopyInteger.setIcon(QIcon("copy-icon.png"))
        self.buttonAboutQt.setIcon(QIcon("qt-icon.png"))
        self.buttonAbout.setIcon(QIcon("information-icon.png"))
        self.buttonAboutQt.setIconSize(QSize(24,24))
        self.buttonAbout.setIconSize(QSize(24,24))
        
        
        # Signals & Slots
        self.buttonBackspace.clicked.connect(self.romanBackspace)
        self.buttonCopyRoman.clicked.connect(self.copyRoman)
        self.buttonCopyInteger.clicked.connect(self.copyInteger)
        self.buttonAboutQt.clicked.connect(self.app.aboutQt)
        self.buttonAbout.clicked.connect(self.aboutProgram)
        self.buttonI.clicked.connect(self.insertI)
        self.buttonV.clicked.connect(self.insertV)
        self.buttonX.clicked.connect(self.insertX)
        self.buttonL.clicked.connect(self.insertL)
        self.buttonC.clicked.connect(self.insertC)
        self.buttonD.clicked.connect(self.insertD)
        self.buttonM.clicked.connect(self.insertM)
        
        
    
    def getAnswer(self):
        answer = 0
        i = 0
        s = self.romanNumber.text()
        
        if s == "":
            self.integerNumber.setText("Empty")
        while (i<len(s)):
            if s[i:i+2] in self.conversion:
                answer += self.conversion[s[i:i+2]]
                i += 2
                self.integerNumber.setText(str(answer))
            else:
                answer += self.conversion[s[i]]
                i +=1
                self.integerNumber.setText(str(answer))
    
    
    
    def romanBackspace(self):
        self.romanNumber.backspace()
        self.getAnswer()
    
    def copyRoman(self):
        self.romanNumber.selectAll()
        self.romanNumber.copy()
        
    def copyInteger(self):
        clip = QApplication.clipboard()
        clip.setText(self.integerNumber.text())
    
    
    def insertI(self):
        print("Button <<I>> Clicked")
        self.romanNumber.setText(self.romanNumber.text() + "I")
        self.getAnswer()
    
    def insertV(self):
        print("Button <<V>> Clicked")
        self.romanNumber.setText(self.romanNumber.text() + "V")
        self.getAnswer()
    
    def insertX(self):
        print("Button <<X>> Clicked")
        self.romanNumber.setText(self.romanNumber.text() + "X")
        self.getAnswer()
        
    def insertL(self):
        print("Button <<L>> Clicked")
        self.romanNumber.setText(self.romanNumber.text() + "L")
        self.getAnswer()
    
    def insertC(self):
        print("Button <<C>> Clicked")
        self.romanNumber.setText(self.romanNumber.text() + "C")
        self.getAnswer()
        
    def insertD(self):
        print("Button <<D>> Clicked")
        self.romanNumber.setText(self.romanNumber.text() + "D")
        self.getAnswer()
    
    def insertM(self):
        print("Button <<M>> Clicked")
        self.romanNumber.setText(self.romanNumber.text() + "M")
        self.getAnswer()
        
    def aboutProgram(self):
        self.DialogAboutProgram = QDialog(self)
        self.DialogAboutProgram.setWindowTitle("About RomanToInteger")
        self.DialogAboutProgram.resize(400,300)
        self.DialogAboutProgram.setWindowIcon(QIcon("Icons\RomanToInteger-icon.png"))
        
        self.aboutProgram = QLabel("A Program created with Python and also using PyQt6 Library,\nfor converting Roman numbers to Integer\n\n\nGitHub: \n\n\n\nLicense:\n    RomanToInteger © 2024 by Gm is licensed under CC BY-SA 4.0\n\nCreated with ❤️ By Gm\n\nVersion: 0.1.0", self.DialogAboutProgram)
        self.aboutProgram.move(20,25)
        
        self.linkLabel = QLabel("<a href=\https://www.github.com/GmPlus24>https://www.github.com/GmPlus24</a>", self.DialogAboutProgram)
        self.linkLabel.setOpenExternalLinks(True)
        self.linkLabel.move(40, 105)
        
        self.DialogAboutProgram.exec()
        


print(">>> out of debug mode")
kernel32 = ctypes.WinDLL('kernel32')
user32 = ctypes.WinDLL('user32')
SW_HIDE = 0
hWnd = kernel32.GetConsoleWindow()
user32.ShowWindow(hWnd, SW_HIDE)


myApp = QApplication(sys.argv)
window = RomanToInteger(myApp)
window.show()
sys.exit(myApp.exec())