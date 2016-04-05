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
#  Both do the same thing
# grid.addWidget(QLabel('Title'), 0, 0)
# lb = QLabel('Title')
# grid.addWidget(lb, 0, 0)
# Both do the same thing

grid.addWidget(QLabel('Title'), 0, 0)
grid.addWidget(QLabel('Author'), 1, 0)
grid.addWidget(QLabel('Review'), 2, 0)


grid.addWidget(QLineEdit(), 0, 1)  # line input for Title QLabel
grid.addWidget(QLineEdit(), 1, 1)  # line input for Author Qlabel
grid.addWidget(QTextEdit(), 2, 1)  # large input for Review Qlabel





#########################
window.show()
app.exec_()
#########################
