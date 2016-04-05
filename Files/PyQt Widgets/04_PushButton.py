from PyQt4.QtCore import *
from PyQt4.QtGui import *

import sys


app = QApplication(sys.argv)

window = QWidget()



window.setWindowTitle('Hello PyQT')
window.setWindowIcon(QIcon('pyqt.png'))
window.setGeometry(50,50,600,400)

button = QPushButton('Close', window)
button.resize(200, 100)
button.move(50,100)
button.clicked.connect(exit)

window.show()
app.exec_()
