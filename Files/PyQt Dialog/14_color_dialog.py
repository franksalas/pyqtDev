from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Hello PyQT')
window.setWindowIcon(QIcon('pyqt.png'))
window.setGeometry(50, 50, 600, 400)


def show_colors():
    cd = QColorDialog.getColor()



bt = QPushButton(window, text='Colors')
bt.move(200,180)
bt.resize(80,30)
bt.clicked.connect(show_colors)



window.show()
app.exec_()