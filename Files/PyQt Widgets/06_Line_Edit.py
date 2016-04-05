from PyQt4.QtCore import *
from PyQt4.QtGui import *

import sys


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Hello PyQT')
window.setWindowIcon(QIcon('pyqt.png'))
window.setGeometry(50,50,600,400)

line_edit = QLineEdit(window)
line_edit.resize(200,50)
line_edit.move(200,100)
#line_edit.setText('PyQt On Udemy')
line_edit.setPlaceholderText('Enter Your name')
line_edit.setEchoMode(QLineEdit.Password)


window.show()
app.exec_()
