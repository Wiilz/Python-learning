import sys
from PyQt4 import QtCore, QtGui, uic     #导入所需的PyQt库

form_class = uic.loadUiType("tempconv_menu.ui")[0]   #加载UI定义

class MyWindowClass(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.btn_CtoF.clicked.connect(self.btn_CtoF_clicked) #将事件处理器与事件相连接
        self.btn_FtoC.clicked.connect(self.btn_FtoC_clicked)
        self.actionC_to_F.triggered.connect(self.btn_CtoF_clicked)
        self.actionF_to_C.triggered.connect(self.btn_FtoC_clicked)
        self.actionExit.triggered.connect(self.menuExit_selected)

    def btn_CtoF_clicked(self):    #CtoF按钮的事件处理器
        cel = float(self.editCel.text())
        fahr = cel * 9 / 5.0 + 32
        self.spinFahr.setValue(int(fahr + 0.5))        

    def btn_FtoC_clicked(self):
        fahr = self.spinFahr.value()
        cel = (fahr - 32)*5 / 9.0
        self.editCel.setText(str(cel))
    def menuExit_selected(self):
        self.close()

app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_()
