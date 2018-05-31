# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(606, 620)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.directorybtn = QtWidgets.QPushButton(self.centralwidget)
        self.directorybtn.setObjectName("directorybtn")
        self.verticalLayout.addWidget(self.directorybtn)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.filterBox = QtWidgets.QComboBox(self.centralwidget)
        self.filterBox.setObjectName("filterBox")
        self.verticalLayout.addWidget(self.filterBox)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.fpsBox = QtWidgets.QComboBox(self.centralwidget)
        self.fpsBox.setObjectName("fpsBox")
        self.verticalLayout.addWidget(self.fpsBox)
        self.startbtn = QtWidgets.QPushButton(self.centralwidget)
        self.startbtn.setObjectName("startbtn")
        self.verticalLayout.addWidget(self.startbtn)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Video Creator"))
        self.directorybtn.setText(_translate("MainWindow", "Select Directory"))
        self.label_2.setText(_translate("MainWindow", "Filter"))
        self.label.setText(_translate("MainWindow", "Frames Per Second"))
        self.startbtn.setText(_translate("MainWindow", "Start"))

