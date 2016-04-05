from PyQt4.QtCore import *
from PyQt4.QtGui import *

import sys


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Hello PyQT')
window.setWindowIcon(QIcon('pyqt.png'))
window.setGeometry(50, 50, 600, 400)

rd = QRadioButton(window,text='PyQt')
rd.move(200, 150)

rd2 = QRadioButton(window,text='Kivy')
rd2.move(200, 190)

checkbox = QCheckBox(window, text='PyQt')
checkbox.move(280, 150)

checkbox2 = QCheckBox(window, text='Kivy')
checkbox2.move(280,190)

window.show()
app.exec_()
