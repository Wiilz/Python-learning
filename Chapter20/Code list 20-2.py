import sys
from PyQt4 import QtCore, QtGui, uic     #导入所需的PyQt库

from_class = uic.loadUiType("MyFirstGui.ui")[0]   #加载在Designer中创建的UI

class MyWindowClass(QtGui.QMainWindow, from_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.button_clicked) #将事件处理器与事件相连接
    def button_clicked(self):
        x = self.pushButton.x()
        y = self.pushButton.y()
        x += 50
        y += 50
        self.pushButton.move(x,y)

app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass()
myWindow.show()
app.exec_()
