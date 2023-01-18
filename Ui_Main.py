import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import numtoword as nw

class Ui_main(QWidget):
    def init(self):
        self.resize(30 ,10)
        self.setWindowTitle('Simple UI')
        self.label = QLabel()
        self.label.setText('Number: ')
        num = QLineEdit()
        num.setValidator(QIntValidator())
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(num)
        num.text
        self.lnum = QTextEdit()
        self.lnum.setReadOnly(True)
        self.lnum.setStyleSheet('background-color:black; color:white; padding-left:5')
        num.textEdited.connect(self.onChange)
        self.vbox.addWidget(self.lnum)
        self.setLayout(self.vbox)
		
    def onChange(self, num):
        value = nw.numtoword(num)
        self.lnum.setText(value)
        self.vbox.addWidget(self.lnum)
		
		
		
if __name__ == '__main__':
	app = QApplication(sys.argv)
	ui = Ui_main()
	ui1 = ui.init()
	ui.show()
	sys.exit(app.exec_())
	