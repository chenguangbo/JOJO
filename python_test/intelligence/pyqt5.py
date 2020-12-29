# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

dict = {'Apple':['iphone7','iphone8','iphone9','iphone10','iphone11'],'HuaWei':['nova 7 Pro','P40Pro','Mate30 Pro','','P30Pro'],
        '小米':['小米10','小米10 Pro','小米8','小米9 SE','小米10 青春版','小米9 Pro'],'vivo':['vivo X50 Pro','vivo X50','vivo S6','vivo Z6']}

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        #MainWindow框体大小
        MainWindow.resize(1100, 850)
        #修改主题的颜色
        palette1 = QtGui.QPalette()
        palette1.setColor(palette1.Window, QtGui.QColor(47, 57, 76))
        MainWindow.setPalette(palette1)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        #comboBox 框体位置和大小
        self.comboBox.setGeometry(QtCore.QRect(310, 20, 91, 31))
        self.comboBox.setObjectName("comboBox")
        # self.comboBox.addItem('Apple')  #添加一个项目
        # self.comboBox.addItem('HuaWei')
        # self.comboBox.addItem('小米')
        # self.comboBox.addItem('vivo')
        self.comboBox.addItems(['Apple', 'HuaWei', '小米', 'vivo'])  # 添加多个项目

        #comboBox关联
        self.comboBox.currentIndexChanged.connect(self.selectionchange)

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(160, 70, 421, 681))
        self.listWidget.setObjectName("listWidget")

        #listWidget双击关联
        self.listWidget.doubleClicked.connect(self.deleteList)

        #获取当前comboBox的text值
        value = self.comboBox.currentText()
        self.listWidget.addItems(dict[value])

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(320, 770, 71, 31))
        #修改button字体大小
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        # 清空
        self.pushButton.clicked.connect(self.empty)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(810, 440, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        #新增一行
        self.pushButton_2.clicked.connect(self.addline)

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(680, 150, 311, 271))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        #设置table行数
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnWidth(0, 100)  # 设置1列的宽度
        self.tableWidget.setColumnWidth(1, 200)  # 设置2列的宽度

        self.tableWidget.setItem(0, 0, QTableWidgetItem("test"))  # 设置0行0列的内容为test

        #后面命名用的列
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)

        MainWindow.setCentralWidget(self.centralwidget)

        #菜单栏和工具栏代码，不需要删除
        # self.menubar = QtWidgets.QMenuBar(MainWindow)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 1221, 23))
        # self.menubar.setObjectName("menubar")
        # MainWindow.setMenuBar(self.menubar)
        # self.statusbar = QtWidgets.QStatusBar(MainWindow)
        # self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "测试"))
        self.pushButton.setText(_translate("MainWindow", "清空"))
        self.pushButton_2.setText(_translate("MainWindow", "新增"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "列一"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "列二"))


    def deleteList(self):
        item = self.listWidget.currentItem()  #获取当前选中对象
        print(item.text())
        self.listWidget.takeItem(self.listWidget.currentRow())  # 删除指定索引号的项目


    def selectionchange(self):
        value = self.comboBox.currentText()
        print("Combo Box显示内容变化，目前显示为{}".format(value))
        self.listWidget.clear()
        list = dict[value]
        self.listWidget.addItems(list)


    def empty(self):
        #listWidget内容清空
        self.listWidget.clear()

    def addline(self):
        row = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(row + 1)
        #滚动条移到最后面
        self.tableWidget.verticalScrollBar().setSliderPosition(row)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())