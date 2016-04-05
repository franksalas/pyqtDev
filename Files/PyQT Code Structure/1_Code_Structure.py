from PyQt4.QtCore import *
from PyQt4.QtGui import *

import sys


app = QApplication(sys.argv)

window = QWidget()
window.show()  # need for window show

app.exec_()
