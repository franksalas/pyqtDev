from PyQt4.QtCore import *
from PyQt4.QtGui import *

import sys


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Hello PyQT')
window.setWindowIcon(QIcon('pyqt.png'))
window.setGeometry(50, 50, 600, 400)

cm = QComboBox(window)
cm.move(200, 200)
cm.resize(200, 50)
cm.addItem('Pyqt')
cm.addItem('Kiviy')
cm.addItem('wx')
cm.addItem('Pyside')
cm.setCurrentIndex(3)


window.show()
app.exec_()