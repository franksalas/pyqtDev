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

grid = QGridLayout(window)

grid.addWidget(QPushButton('Bttn [0][0]'), 0, 0)
grid.addWidget(QPushButton('Bttn [0][1]'), 0, 1)
grid.addWidget(QPushButton('Bttn [1][0]'), 1, 0)
grid.addWidget(QPushButton('Bttn [1][0]'), 1, 0)
grid.addWidget(QPushButton('Bttn [2][1]'), 2, 1)
grid.addWidget(QPushButton('Bttn [2][1]'), 2, 1)
grid.addWidget(QPushButton('Bttn [3][2]'), 3, 2)
grid.addWidget(QLineEdit(), 0, 2)







#########################
window.show()
app.exec_()
#########################
