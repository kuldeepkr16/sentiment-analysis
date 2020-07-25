# Sentiment analysis
from textblob import TextBlob
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        btn = QPushButton('ANALYSE',self)
        btn.move(150,300)
        btnq = QPushButton('EXIT', self)
        btnq.move(230, 300)
        btnq.clicked.connect(QCoreApplication.instance().quit)
        self.textbox = QLineEdit(self)
        self.textbox.move(80, 20)
        self.textbox.resize(280, 40)
        self.textbox.setFont(QFont("Arial",20))
        self.lbl = QLabel(self)
        self.lbl.setGeometry(100, 100, 350, 150)
        btn.clicked.connect(self.edit)
        self.setGeometry(300, 200, 450, 350)
        self.setWindowTitle('Sentiment Analysis')
        self.setWindowIcon(QIcon('images.jpg'))
        self.show()

    #sentiment analysis
    def edit(self):
        msg = self.textbox.text()
        print(msg)
        txt = TextBlob(msg)
        newfont = QFont("Times", 20, QFont.Bold)
        self.lbl.setFont(newfont)
        a = txt.sentiment.polarity
        toprint = ""
        print(a)
        if a > -1 and a < -0.5:
            toprint = "Aww.. What happened??"
        elif a >= -0.5 and a < 0:
            toprint = "This is bad."
        elif a == 0:
            toprint = "What should i say??"
        elif a > 0 and a <= 0.5:
            toprint = "yeah.. that's good."
        elif a > 0.5 and a <= 0.8:
            toprint = "That's nice"
        elif a >0.8 and a <= 1:
            toprint = "wow... that's very nice"
        self.lbl.setText(toprint)
        label = QLabel(self)
        pixmap = QPixmap('images.jpg')
        label.setPixmap(pixmap)
        self.textbox.setText("")

if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())


