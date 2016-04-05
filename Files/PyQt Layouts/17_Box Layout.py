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

ok_button = QPushButton(window, text='OK')
cancel_button = QPushButton(window, text='Cancel')

# hbox = QHBoxLayout(window)
# hbox.addStretch()
# hbox.addWidget(ok_button)
# hbox.addWidget(cancel_button)

vbox = QVBoxLayout(window)
vbox.addStretch()
vbox.addWidget(ok_button)
vbox.addWidget(cancel_button)




#########################
window.show()
app.exec_()
#########################
