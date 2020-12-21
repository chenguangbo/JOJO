# -*- coding: utf-8 -*-

# 逻辑代码参考
# 引入并初始化了外部ui文件的资源，直接运行，可以显示ui

# 导入必备的库
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import  wx
# 导入ui文件，这个名字就是ui文件的名称
from Ui_HelloWorld_Main_Ui import *


# 新建一个“类”，里面的方法主要是对UI的业务逻辑
class HelloWorld(QMainWindow, Ui_HelloWorld_Main_Ui):  # 括号里面的第二个参数，就是ui文件的类的名称
    def __init__(self, parent=None):
        super(HelloWorld, self).__init__(parent)  # 注意第一个参数，是这个类本身的名字
        self.setupUi(self)  # 初始化窗口


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = HelloWorld()
    myWin.show()
    sys.exit(app.exec_())
