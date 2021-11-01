#!/usr/bin/env python3
# Author: Disequilibrium
# Description: GUI classes and/or instances are defined within this file.

import backend

from PyQt5 import QtCore, QtGui, QtWidgets

## MAIN WINDOW CLASS ##
class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.setWindowModality(QtCore.Qt.NonModal)
        mainWindow.setEnabled(True)
        mainWindow.setFixedSize(370, 330)
        mainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.mainBotPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.mainBotPushButton.setGeometry(QtCore.QRect(30, 210, 311, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.mainBotPushButton.setFont(font)
        self.mainBotPushButton.setObjectName("mainBotPushButton")
        self.mainServerTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.mainServerTableWidget.setGeometry(QtCore.QRect(30, 31, 311, 171))
        self.mainServerTableWidget.setRowCount(0)
        self.mainServerTableWidget.setObjectName("mainServerTableWidget")
        self.mainServerTableWidget.setColumnCount(0)
        self.mainServerLabel = QtWidgets.QLabel(self.centralwidget)
        self.mainServerLabel.setGeometry(QtCore.QRect(30, 10, 281, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.mainServerLabel.setFont(font)
        self.mainServerLabel.setObjectName("mainServerLabel")
        self.mainRefreshPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.mainRefreshPushButton.setGeometry(QtCore.QRect(270, 10, 71, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.mainRefreshPushButton.setFont(font)
        self.mainRefreshPushButton.setObjectName("mainRefreshPushButton")
        mainWindow.setCentralWidget(self.centralwidget)
        self.mainMenuBar = QtWidgets.QMenuBar(mainWindow)
        self.mainMenuBar.setGeometry(QtCore.QRect(0, 0, 370, 21))
        self.mainMenuBar.setObjectName("mainMenuBar")
        self.mainMenuSettings = QtWidgets.QMenu(self.mainMenuBar)
        self.mainMenuSettings.setObjectName("mainMenuSettings")
        self.mainMenuBackup = QtWidgets.QMenu(self.mainMenuBar)
        self.mainMenuBackup.setObjectName("mainMenuBackup")
        mainWindow.setMenuBar(self.mainMenuBar)
        self.mainStatusbar = QtWidgets.QStatusBar(mainWindow)
        self.mainStatusbar.setObjectName("mainStatusbar")
        mainWindow.setStatusBar(self.mainStatusbar)
        self.actionBot_Setup = QtWidgets.QAction(mainWindow)
        self.actionBot_Setup.setObjectName("actionBot_Setup")
        self.actionServer_to_Server = QtWidgets.QAction(mainWindow)
        self.actionServer_to_Server.setObjectName("actionServer_to_Server")
        self.actionServer_to_Local_Disk = QtWidgets.QAction(mainWindow)
        self.actionServer_to_Local_Disk.setObjectName("actionServer_to_Local_Disk")
        self.actionEstablish_LiveSync = QtWidgets.QAction(mainWindow)
        self.actionEstablish_LiveSync.setObjectName("actionEstablish_LiveSync")
        self.actionAbout = QtWidgets.QAction(mainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.mainMenuSettings.addAction(self.actionBot_Setup)
        self.mainMenuSettings.addAction(self.actionAbout)
        self.mainMenuBackup.addAction(self.actionServer_to_Server)
        self.mainMenuBackup.addAction(self.actionServer_to_Local_Disk)
        self.mainMenuBackup.addAction(self.actionEstablish_LiveSync)
        self.mainMenuBar.addAction(self.mainMenuBackup.menuAction())
        self.mainMenuBar.addAction(self.mainMenuSettings.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

        ## MainWindow Functionalities ##
        self.actionAbout.triggered.connect(self.openAbout)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Gemini"))
        self.mainBotPushButton.setText(_translate("mainWindow", "Gemini Status: Offline"))
        self.mainServerLabel.setText(_translate("mainWindow", "Server List:"))
        self.mainRefreshPushButton.setText(_translate("mainWindow", "Refresh"))
        self.mainMenuSettings.setTitle(_translate("mainWindow", "Settings"))
        self.mainMenuBackup.setTitle(_translate("mainWindow", "Backup"))
        self.actionBot_Setup.setText(_translate("mainWindow", "Bot Setup..."))
        self.actionServer_to_Server.setText(_translate("mainWindow", "Server to Server..."))
        self.actionServer_to_Local_Disk.setText(_translate("mainWindow", "Server to Local Disk..."))
        self.actionEstablish_LiveSync.setText(_translate("mainWindow", "Establish LiveSync..."))
        self.actionAbout.setText(_translate("mainWindow", "About..."))

    def openAbout(self):
        AboutDialog = QtWidgets.QDialog()
        AboutDialog.ui = Ui_AboutDialog()
        AboutDialog.ui.setupUi(AboutDialog)
        AboutDialog.exec_()
        AboutDialog.show()


## ABOUT DIALOG CLASS ##
class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName("AboutDialog")
        AboutDialog.setFixedSize(221, 120)
        self.label = QtWidgets.QLabel(AboutDialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 171, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(AboutDialog)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 171, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(AboutDialog)
        self.label_3.setGeometry(QtCore.QRect(30, 60, 171, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(AboutDialog)
        self.label_4.setGeometry(QtCore.QRect(30, 80, 171, 16))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(AboutDialog)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

    def retranslateUi(self, AboutDialog):
        _translate = QtCore.QCoreApplication.translate
        AboutDialog.setWindowTitle(_translate("AboutDialog", "About"))
        self.label.setText(_translate("AboutDialog", "Version: 1.0"))
        self.label_2.setText(_translate("AboutDialog", "Created by: Disequilibrium"))
        self.label_3.setText(_translate("AboutDialog", "Powered by: Python 3"))
        self.label_4.setText(_translate("AboutDialog", "GUI: PyQt5"))


def start():

    import sys
    import qdarkstyle

    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
