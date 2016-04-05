from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
#########################
app = QApplication(sys.argv)
window = QMainWindow()
#########################


#########################
'''
Menu
'''
menu = QMenuBar(window)

file_menu = menu.addMenu('File')
edit_menu = menu.addMenu('Edit')
view_menu = menu.addMenu('View')


new = QAction('New Project', window)
new.setShortcut('ctrl+N')
open = QAction('Open', window)
open.setShortcut('ctrl+O')

file_menu.addAction(new)
file_menu.addAction(open)





#########################
window.show()
app.exec_()
#########################
