from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Hello PyQT')
window.setWindowIcon(QIcon('pyqt.png'))
window.setGeometry(50, 50, 600, 400)


def show_font():
    fd= QFontDialog.getFont()



bt = QPushButton(window, text='Fonts')
bt.move(200,180)
bt.clicked.connect(show_font)


window.show()
app.exec_()