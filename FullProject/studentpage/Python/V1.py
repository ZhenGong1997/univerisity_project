# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'V1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("ProfMate")
        MainWindow.resize(581, 561)
        MainWindow.setAcceptDrops(False)
        icon = QtGui.QIcon.fromTheme("ProfMate")
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(200, 20, 271, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(100, -20, 91, 111))
        self.label_6.setStyleSheet("image: url(:/Logo/MAC.png);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(330, 210, 181, 181))
        self.listWidget_2.setObjectName("listWidget_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 440, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.Percentage = QtWidgets.QProgressBar(self.centralwidget)
        self.Percentage.setGeometry(QtCore.QRect(170, 400, 118, 23))
        self.Percentage.setProperty("value", 24)
        self.Percentage.setObjectName("Percentage")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 110, 91, 31))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(330, 180, 71, 16))
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 180, 71, 16))
        self.label_3.setObjectName("label_3")
        self.listView_2 = QtWidgets.QListView(self.centralwidget)
        self.listView_2.setGeometry(QtCore.QRect(430, 180, 81, 21))
        self.listView_2.setObjectName("listView_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 110, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 80, 91, 31))
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(190, 80, 73, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(210, 180, 81, 21))
        self.listView.setObjectName("listView")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(190, 120, 131, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(110, 210, 181, 181))
        self.listWidget.setObjectName("listWidget")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(410, 440, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 581, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#550022;\">McMaster </span><span style=\" font-size:18pt; font-weight:600; font-style:italic; color:#940049;\">ProfMate</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Save"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Section :</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; color:#ff0000;\">Absent</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; color:#0000ff;\">Attandance </span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "OK"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Lecture :</span></p></body></html>"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "ENG 4A06"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "COMPENG 4TL4"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Section 1001"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Section 1002"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Section 1003"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Section 1004"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Section 1005"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Section 1006"))
        self.pushButton_3.setText(_translate("MainWindow", "Exit"))
import MAC_rc
