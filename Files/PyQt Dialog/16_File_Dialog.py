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
#########################


def upload():
    open_file = QFileDialog.getOpenFileName(window, 'open file')
    print(open_file)
    print()
    print('____________________________')

    with open(open_file, 'r' ) as f:
        print(f.read())

bt = QPushButton(window, text='Upload A File')
bt.move(200, 200)
bt.clicked.connect(upload)


#########################
window.show()
app.exec_()
#########################
