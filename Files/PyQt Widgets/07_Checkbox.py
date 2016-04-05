from PyQt4.QtCore import *
from PyQt4.QtGui import *

import sys


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Hello PyQT')
window.setWindowIcon(QIcon('pyqt.png'))
window.setGeometry(50,50,600,400)

checkbox = QCheckBox(window, text='PyQt')
checkbox.move(200,200)
checkbox.setChecked(True)  # bool = True or False


checkbox2 = QCheckBox(window, text ='kivy')
checkbox2.move(200,250)


window.show()
app.exec_()
