from PyQt4.QtCore import *
from PyQt4.QtGui import *

import sys


app = QApplication(sys.argv)

window = QWidget()

window.show()
window.setWindowTitle('Hello PyQT')
window.setWindowIcon(QIcon('pyqt.png'))

app.exec_()
