from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
#########################
app = QApplication(sys.argv)
window = QWidget()
#########################

window.setWindowTitle('Hello PyQT')
window.setWindowIcon(QIcon('pyqt.png'))
window.setGeometry(50, 50, 600, 400)
window.resize(500,500)
#########################
b1 = QPushButton(window,text='Button1')
b2 = QPushButton(window,text='Button2')
b3 = QPushButton(window,text='Button3')
b4 = QPushButton(window,text='Button4')

vbox = QVBoxLayout(window)
vbox.addWidget(b1)
vbox.addStretch()
vbox.addWidget(b2)

hbox = QHBoxLayout(window)
hbox.addWidget(b3)
hbox.addStretch()
hbox.addWidget(b4)

vbox.addLayout(hbox)  # button 3 button 4 below button1 button2 horisontal.


#########################
window.show()
app.exec_()
#########################
