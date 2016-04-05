from PyQt4.QtCore import *
from PyQt4.QtGui import *

import sys


app = QApplication(sys.argv)
window = QWidget()



window.setWindowTitle('Hello PyQT')
window.setWindowIcon(QIcon('pyqt.png'))
window.setGeometry(50,50,600,400)

#  (qwidget, title, question, controls, defaultvalue)

message = QMessageBox.question(window, "message box", 'Do you want to Exit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

# information, critical, question, warting, about
window.show()
app.exec_()
