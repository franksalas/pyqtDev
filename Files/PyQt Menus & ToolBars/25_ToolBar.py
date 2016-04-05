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
new = QAction(QIcon('pyqt.png'),'New Project', window)
new.setShortcut('ctrl+N')
open = QAction(QIcon('pyqt.png'), 'Open', window)
open.setShortcut('ctrl+O')

close = QAction(QIcon('doc.png'),'Close App', window)
close.triggered.connect(window.close)

'''
SubMenu
'''
sub = QMenu('Open Recent')
sub.addAction('.py')
sub.addAction('.pyc')

file_menu.addAction(new)
file_menu.addAction(open)
file_menu.addMenu(sub)
file_menu.addAction(close)

'''
ToolBar
'''
window.toolBar = window.addToolBar('Exit')
window.toolBar.addAction(close)

window.toolBar = window.addToolBar('Open')
window.toolBar.addAction(open)
window.toolBar.addAction(new)


#########################
window.show()
app.exec_()
#########################