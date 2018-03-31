import sys
from PyQt4 import QtCore, QtGui, uic     #导入所需的PyQt库

form_class = uic.loadUiType("MyFirstGui.ui")[0]   #加载在Designer中创建的UI

class MyWindowClass(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)

app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass()
myWindow.show()
app.exec_()
