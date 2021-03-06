#!/usr/bin/env python3
# Author: Disequilibrium
# Description: Backend functions are defined within this file.

import os
import re
import sys
import json
import time
import asyncio
import signal


import gui

import discord
from discord.utils import get
from discord.ext import commands, tasks

from threading import Thread

## GLOBAL VARIABLES ##
intents = intents = discord.Intents.default()
bot = commands.Bot(command_prefix = '=/=', intents=intents)

## GLOBAL VARIABLES ##

## EXCEPTION CLASSES ##
class InvalidToken(Exception):
    pass
class ConfigDoesNotExist(Exception):
    pass
class ConnectionFailed(Exception):
    pass
class BotExistsInNoServers(Exception):
    pass
class EmptyField(Exception):
    pass
class InvalidFieldFormat(Exception):
    pass
class BotNotPresentInServer(Exception):
    pass
class SameSourceAndTarget(Exception):
    pass
## EXCEPTION CLASSES ##

# Bot launch procedure
def startGemini(mainDialog):

    # Check if config file exists
    if not os.path.exists("../../configs/configs.json"):
        raise ConfigDoesNotExist

    startButton = mainDialog.mainBotPushButton
    startButton.setEnabled(False)
    startButton.setText("Initializing Gemini...")

    with open("../../configs/configs.json", "r") as configFile:
        config = json.load(configFile)
        token = config['TOKEN']
        timeout = config['TIMEOUT']
        validateAPIToken(token)
        configFile.close()

    # Launch bot in separate thread in daemon mode
    # When application closes, all threads close automatically
    bot_thread = Thread(target = bot.run, args = (token,))
    bot_thread.daemon = True
    bot_thread.start()

    # To-do: Correct this by handling exceptions that happen within separate threads.
    time.sleep(timeout)

    if startButton.text() == "Initializing Gemini...":
        raise ConnectionFailed

# Save the given API token to the config file
def saveBotSetup(setupDialog):
    keyTextField = setupDialog.setupLineEdit
    timeSpinBox = setupDialog.timeoutSpinBox

    token = keyTextField.text().replace(' ','').replace('\t','')
    timeout = int(timeSpinBox.text())
    validateAPIToken(token)

    setup = {
        "TOKEN": token,
        "TIMEOUT": timeout
    }

    with open("../../configs/configs.json", "w") as configFile:
        configFile.write(json.dumps(setup, indent = 4))
        configFile.close()

# Refresh the list of servers on the Main Window
def refreshServerList(mainDialog, qtWidgets):

    servers = bot.guilds
    if len(servers) == 0:
        raise BotExistsInNoServers

    tableWidget = mainDialog.mainServerTableWidget

    row = 0
    tableWidget.setRowCount(len(servers))

    for server in servers:
        tableWidget.setItem(row, 0, qtWidgets.QTableWidgetItem(str(server.id)))
        tableWidget.setItem(row, 1, qtWidgets.QTableWidgetItem(server.name))
        row += 1

# Validate the format of the given API token
# XXXXXXXXXXXXXXXXXXXXXXXX.XXXXXX.XXXXXXXXXXXXXXXXXXXXXXXXXXX
# Case Un-sensitive alphanumeric
def validateAPIToken(token):
    if not bool(re.match('^([a-zA-Z0-9_-]{24})\.([a-zA-Z0-9_-]{6})\.([a-zA-Z0-9_-]{27})$', token)):
        raise InvalidToken

# Server to Server Clone Function
def startCloning(ssDialog):
    sourceServerID = ssDialog.sourceLineEdit.text().replace(' ','').replace('\t','')
    targetServerID = ssDialog.targetLineEdit.text().replace(' ','').replace('\t','')
    messageBool = ssDialog.messageCheckBox.isChecked()
    numberOfMessages = ssDialog.messageSpinBox.text().replace(' ','').replace('\t','')
    attachmentBool = ssDialog.attachmentCheckBox.isChecked()
    emojiBool = ssDialog.emojiCheckBox.isChecked()
    roleBool = ssDialog.rolesCheckBox.isChecked()

    # Checking for Exceptions
    if len(sourceServerID) == 0 or len(targetServerID) == 0:
        raise EmptyField
    if not bool(re.match('^[0-9]*$', sourceServerID)) or not bool(re.match('^[0-9]*$', targetServerID)):
        raise InvalidFieldFormat

    serverIDList = []
    for server in bot.guilds:
        serverIDList.append(server.id)
    print(serverIDList)
    if (not int(sourceServerID) in serverIDList) or (not int(targetServerID) in serverIDList):
        raise BotNotPresentInServer
    if int(sourceServerID) == int(targetServerID):
        raise SameSourceAndTarget

    progressDialog = ssDialog.startProgress()

# This Function serves as await, without having to turn the whole function into an async one
def await_this(function):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    return loop.run_until_complete(function)

# Triggered when bot is started
@bot.event
async def on_ready():

    # Set the text on the main status button when ready
    gui.ui.mainBotPushButton.setText("Gemini Initialized.\n\n (Bot ID: " + str(bot.user.id) + ")")
