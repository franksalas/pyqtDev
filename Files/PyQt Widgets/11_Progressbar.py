from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Hello PyQT')
window.setWindowIcon(QIcon('pyqt.png'))
window.setGeometry(50, 50, 600, 400)

pb = QProgressBar(window)
pb.move(200, 180)
pb.resize(300, 50)
pb.setValue(20)
pb.setAlignment(Qt.AlignCenter)



window.show()
app.exec_()