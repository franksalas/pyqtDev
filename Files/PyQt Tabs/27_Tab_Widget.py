from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
#########################
app = QApplication(sys.argv)
tabs = QTabWidget()  # QTabWidget()
#########################

#########################
tab1 = QWidget()
tab2 = QWidget()
tab3 = QWidget()



vbox = QVBoxLayout(tabs)
b1 = QPushButton('Ok')
b2 = QPushButton('Cancel')
vbox.addWidget(b1)
vbox.addStretch()
vbox.addWidget(b2)

vbox2 = QVBoxLayout(tabs)
line1 = QLineEdit()
label1 = QLabel("Welcome")
vbox2.addWidget(line1)
vbox2.addWidget(label1)


hbox = QHBoxLayout(tabs)
lc = QLCDNumber()
d = QDial()
hbox.addWidget(lc)
hbox.addWidget(d)



tab1.setLayout(vbox)    # adds vertical to tab1
tab2.setLayout(vbox2)
tab3.setLayout(hbox)


tabs.addTab(tab1, 'File ')
tabs.addTab(tab2, 'Save ')
tabs.addTab(tab3, 'Settings')


#########################
tabs.show()
app.exec_()
#########################