#!/usr/bin/env python3
# Author: Disequilibrium
# Description: GUI classes and/or instances are defined within this file.

import backend

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

## MAIN WINDOW CLASS ##
class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.setWindowModality(QtCore.Qt.NonModal)
        mainWindow.setEnabled(True)
        mainWindow.setFixedSize(370, 335)
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
        self.mainServerTableWidget.setWhatsThis("")
        self.mainServerTableWidget.setRowCount(0)
        self.mainServerTableWidget.setColumnCount(2)
        self.mainServerTableWidget.setObjectName("mainServerTableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.mainServerTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.mainServerTableWidget.setHorizontalHeaderItem(1, item)
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
        self.actionBot_Setup.setEnabled(True)
        self.actionBot_Setup.setObjectName("actionBot_Setup")
        self.actionServer_to_Server = QtWidgets.QAction(mainWindow)
        self.actionServer_to_Server.setObjectName("actionServer_to_Server")
        self.actionServer_to_Local_Disk = QtWidgets.QAction(mainWindow)
        self.actionServer_to_Local_Disk.setObjectName("actionServer_to_Local_Disk")
        self.actionLocal_Disk_to_Server = QtWidgets.QAction(mainWindow)
        self.actionLocal_Disk_to_Server.setObjectName("actionLocal_Disk_to_Server")
        self.actionEstablish_LiveSync = QtWidgets.QAction(mainWindow)
        self.actionEstablish_LiveSync.setObjectName("actionEstablish_LiveSync")
        self.actionAbout = QtWidgets.QAction(mainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.mainMenuSettings.addAction(self.actionBot_Setup)
        self.mainMenuSettings.addAction(self.actionAbout)
        self.mainMenuBackup.addAction(self.actionServer_to_Server)
        self.mainMenuBackup.addAction(self.actionServer_to_Local_Disk)
        self.mainMenuBackup.addAction(self.actionLocal_Disk_to_Server)
        self.mainMenuBackup.addAction(self.actionEstablish_LiveSync)
        self.mainMenuBar.addAction(self.mainMenuBackup.menuAction())
        self.mainMenuBar.addAction(self.mainMenuSettings.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

        ## MainWindow Functionalities ##
        self.actionAbout.triggered.connect(self.openAbout)
        self.actionBot_Setup.triggered.connect(self.openBotSetup)
        self.mainBotPushButton.clicked.connect(self.startGemini)
        self.mainRefreshPushButton.clicked.connect(self.refreshServerList)

        self.mainRefreshPushButton.setEnabled(False)
        self.actionServer_to_Server.setEnabled(False)
        self.actionServer_to_Local_Disk.setEnabled(False)
        self.actionLocal_Disk_to_Server.setEnabled(False)
        self.actionEstablish_LiveSync.setEnabled(False)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Gemini"))
        self.mainBotPushButton.setText(_translate("mainWindow", "Gemini Status: Offline"))
        item = self.mainServerTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("mainWindow", "Server ID"))
        item = self.mainServerTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("mainWindow", "Server Name"))
        self.mainServerLabel.setText(_translate("mainWindow", "Server List:"))
        self.mainRefreshPushButton.setText(_translate("mainWindow", "Refresh"))
        self.mainMenuSettings.setTitle(_translate("mainWindow", "Settings"))
        self.mainMenuBackup.setTitle(_translate("mainWindow", "Backup"))
        self.actionBot_Setup.setText(_translate("mainWindow", "Bot Setup..."))
        self.actionServer_to_Server.setText(_translate("mainWindow", "Clone from Server to Server..."))
        self.actionServer_to_Local_Disk.setText(_translate("mainWindow", "Backup from Server to Local Disk..."))
        self.actionLocal_Disk_to_Server.setText(_translate("mainWindow", "Restore from Local Disk to Server..."))

        self.actionEstablish_LiveSync.setText(_translate("mainWindow", "Establish LiveSync..."))
        self.actionAbout.setText(_translate("mainWindow", "About..."))

    def openAbout(self):
        AboutDialog = QtWidgets.QDialog()
        AboutDialog.ui = Ui_AboutDialog()
        AboutDialog.ui.setupUi(AboutDialog)
        AboutDialog.exec_()
        AboutDialog.show()

    def openBotSetup(self):
        SetupDialog = QtWidgets.QDialog()
        SetupDialog.ui = Ui_SetupDialog()
        SetupDialog.ui.setupUi(SetupDialog)
        SetupDialog.exec_()
        SetupDialog.show()

    def startGemini(self):
        try:
            backend.startGemini(self.mainBotPushButton)
            self.mainRefreshPushButton.setEnabled(True)
            self.actionServer_to_Server.setEnabled(True)
            self.actionServer_to_Local_Disk.setEnabled(True)
            self.actionLocal_Disk_to_Server.setEnabled(True)
            self.actionEstablish_LiveSync.setEnabled(True)
        except backend.InvalidToken:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Invalid API Key.")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()
            self.mainBotPushButton.setText("Start Gemini")
            self.mainBotPushButton.setEnabled(True)
        except backend.ConfigDoesNotExist:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Config File does not exist.\nTry setting up the Bot first.")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()
            self.mainBotPushButton.setText("Start Gemini")
            self.mainBotPushButton.setEnabled(True)
        except backend.ConnectionFailed:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Connection Failed.\nEither you should:\n\t- Fix the API Key and restart the application\n\t- Increase the Connection Timeout")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()
            self.mainBotPushButton.setText("Start Gemini")
            self.mainBotPushButton.setEnabled(True)

    def refreshServerList(self):
        try:
            backend.refreshServerList(self.mainRefreshPushButton, self.mainServerTableWidget, QtWidgets)
        except backend.BotExistsInNoServers:
            msg = QMessageBox()
            msg.setWindowTitle("Warning")
            msg.setText("Bot is not a member of any Discord Servers.")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()

## BOT SETUP DIALOG CLASS ##
class Ui_SetupDialog(object):
    def setupUi(self, SetupDialog):
        SetupDialog.setObjectName("SetupDialog")
        SetupDialog.setFixedSize(401, 120)
        self.setupLineEdit = QtWidgets.QLineEdit(SetupDialog)
        self.setupLineEdit.setGeometry(QtCore.QRect(20, 30, 361, 20))
        self.setupLineEdit.setInputMask("")
        self.setupLineEdit.setText("")
        self.setupLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.setupLineEdit.setObjectName("setupLineEdit")
        self.label = QtWidgets.QLabel(SetupDialog)
        self.label.setGeometry(QtCore.QRect(150, 10, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.setupSavePushButton = QtWidgets.QPushButton(SetupDialog)
        self.setupSavePushButton.setGeometry(QtCore.QRect(140, 90, 111, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.setupSavePushButton.setFont(font)
        self.setupSavePushButton.setObjectName("setupSavePushButton")
        self.label_2 = QtWidgets.QLabel(SetupDialog)
        self.label_2.setGeometry(QtCore.QRect(90, 60, 121, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.timeoutSpinBox = QtWidgets.QSpinBox(SetupDialog)
        self.timeoutSpinBox.setGeometry(QtCore.QRect(220, 60, 42, 16))
        self.timeoutSpinBox.setProperty("value", 5)
        self.timeoutSpinBox.setObjectName("timeoutSpinBox")
        self.label_3 = QtWidgets.QLabel(SetupDialog)
        self.label_3.setGeometry(QtCore.QRect(270, 60, 41, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(SetupDialog)
        QtCore.QMetaObject.connectSlotsByName(SetupDialog)

        ## SetupDialog Functionalities ##
        self.setupSavePushButton.clicked.connect(self.saveBotSetup)
        self.setupLineEdit.textChanged.connect(self.enableSaveButton)
        self.timeoutSpinBox.textChanged.connect(self.enableSaveButton)

    def retranslateUi(self, SetupDialog):
        _translate = QtCore.QCoreApplication.translate
        SetupDialog.setWindowTitle(_translate("SetupDialog", "Bot Setup"))
        self.setupLineEdit.setPlaceholderText(_translate("SetupDialog", "XXXXXXXXXXXXXXXXXXXXXXXX.XXXXXX.XXXXXXXXXXXXXXXXXXXXXXXXXXX"))
        self.label.setText(_translate("SetupDialog", "Bot API Token:"))
        self.setupSavePushButton.setText(_translate("SetupDialog", "Save"))
        self.label_2.setText(_translate("SetupDialog", "Connection Timeout:"))
        self.label_3.setText(_translate("SetupDialog", "Seconds"))

    def enableSaveButton(self):
        self.setupSavePushButton.setText("Save")
        self.setupSavePushButton.setEnabled(True)

    def saveBotSetup(self):
        try:
            backend.saveBotSetup(self.setupSavePushButton, self.setupLineEdit, self.timeoutSpinBox)
            self.setupSavePushButton.setText("Saved!")
            self.setupSavePushButton.setEnabled(False)

        except backend.InvalidToken:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Invalid API Key.")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()

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
    global ui
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    ret = app.exec_()

    # Things to do before quitting the application

    sys.exit(ret)
