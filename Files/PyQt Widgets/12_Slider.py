from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Hello PyQT')
window.setWindowIcon(QIcon('pyqt.png'))
window.setGeometry(50, 50, 600, 400)

sl = QSlider(window)
sl.move(100,180)
sl.resize(20, 180)
sl.setValue(50)


sl2 = QSlider(Qt.Horizontal, window)
sl2.move(200, 180)
sl2.resize(180, 20)
sl2.setValue(30)





window.show()
app.exec_()