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
# window.resize(500, 500)
#########################
'''
Signal is the button
Slots is the function that will be executed
when you press that button.
'''

s = QSlider(window)
s.move(330,30)

d = QDial(window)
d.move(30,30)

button = QPushButton(window, text = 'Change value')
button.move(200, 300)


def change_slider_value():
    s.setValue(50)


button.clicked.connect(change_slider_value)

s.valueChanged.connect(d.setValue)
d.valueChanged.connect(s.setValue)





#########################
window.show()
app.exec_()
#########################
