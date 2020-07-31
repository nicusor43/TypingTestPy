import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import PyQt5.QtCore

from random import randint

word_list = []

f = open("words.txt", "r", encoding="utf-8")

for line in f:
    if len(line) > 2:
        word_list.append(line)

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Typing Test'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 400
        self.wpm = 0
        self.words_correct = 0
        self.game_end = False
        self.initUI()
        
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
    
        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(100, 200)
        self.textbox.resize(200,40)
        self.textbox.textChanged.connect(self.textchanged)


        self.score = QLabel(self)
        self.score.move(150,100)
        self.score.resize(100, 60)
        self.score.setStyleSheet('background-color: white; color: black')
        self.score.setAlignment(Qt.AlignTop)
        self.score.setText(f" WPM")

        self.text = QLabel(self)
        self.text.move(140,20)
        self.text.resize(120, 60)
        self.text.setStyleSheet('background-color: black; color: white')
        self.text.setAlignment( Qt.AlignTop)
        self.text.setFont(QFont("SansSerif", 15))
        self.text.setText(word_list[randint(0, 900)])

        self.startbutton = QPushButton(self)
        self.startbutton.setText("Start")
        self.startbutton.move(175, 300)
        self.startbutton.resize(50,30)
        self.startbutton.setStyleSheet('background-color: black; color: white')
        self.startbutton.clicked.connect(self.startgame)
        self.show()

    def textchanged(self):
        if not self.game_end:
            idk = self.textbox.text()
            if len(idk) > 0:
                if idk[-1] == " ":
                    self.textbox.clear()
                    if idk[:-1] == str(self.text.text()[:-1]):
                        self.words_correct += 1
                        self.score.setText(f"{int(self.words_correct / (60000 -  timer.remainingTime()) * 60000)} WPM")
                        self.text.setText(word_list[randint(0,900)])
                        print(timer.remainingTime())
        

    def startgame(self):
        global timer 
        timer = QTimer()
        timer.start(60000)
        timer.timeout.connect(self.end)
        
        

    def end(self):
        self.game_end = True
        self.score.setText(f"{self.words_correct / 60} WPM ")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())



