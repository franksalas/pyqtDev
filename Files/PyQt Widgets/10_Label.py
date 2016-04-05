from PyQt4.QtCore import *
from PyQt4.QtGui import *

import sys


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Hello PyQT')
window.setWindowIcon(QIcon('pyqt.png'))
window.setGeometry(50, 50, 600, 400)

lb = QLabel(window, text='UserName')
lb.move(100, 180)

lb2 = QLabel(window, text='Password')
lb2.move(100, 220)

le = QLineEdit(window)
le.move(180, 180)

le2 = QLineEdit(window)
le2.move(180, 220)
le2.setEchoMode(QLineEdit.Password)
window.show()
app.exec_()