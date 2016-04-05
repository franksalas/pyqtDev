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

p = QPushButton(window,text='Welcome')

#p.move(200, 200)
# p.setGeometry(ypos,xpos,width, height)
p.setGeometry(150, 150, 80, 40)




#########################
window.show()
app.exec_()
#########################
