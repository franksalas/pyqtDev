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
window.resize(500, 500)
#########################
'''
Signal is the button
Slots is the function that will be executed
when you press that button.
'''


button = QPushButton(window, text='Login')
button.move(80, 100)
button.resize(90, 60)

slider = QSlider(window)
slider.move(190,100)
slider.setValue(30)


def button_clicked():
    print('Button Clicked')
    slider.setValue(50)  # move slider to 50%c

button.clicked.connect(button_clicked)  # prints on console.


#########################
window.show()
app.exec_()
#########################
