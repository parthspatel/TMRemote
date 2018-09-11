import os
import pickle
import re
import sys

import requests
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from backend.auth import Auth
from backend.log import Log


class downloadUpdates(QThread):
    def __init__(self, username, password, apikey, tmPath, logs, links):
        QThread.__init__(self)
        self.getUsername = username
        self.getPassword = password
        self.apiKey = apikey

        self.getTmPath = tmPath
        self.logs = logs

        self.links = links

        self.sleep_time = 60
        self.sleep_time_const = 10

    def __del__(self):
        self.wait()

    def __checkTerminalScripts(self):
        tmPath = self.getTmPath().split('TerminalManager.exe')[0]
        if self.getTmPath() is None:
            return 'Error: Terminal Manager folder is not selected'
        scriptsFolder = tmPath + 'TMRemote/Scripts'
        tmRemoteFolder = tmPath + 'TMRemote'
        if not os.path.isdir(tmRemoteFolder):
            os.mkdir(tmRemoteFolder)
        if not os.path.isdir(scriptsFolder):
            os.mkdir(scriptsFolder)
        if not scriptsFolder in sys.path:
            sys.path.append(scriptsFolder)
        self.__downloadModule()
        self.__downloadScript()

    def __downloadScript(self, token=None):
        tmPath = self.getTmPath()
        scriptPath = tmPath.replace(
            'TerminalManager.exe', 'TMRemote/Scripts/Logger.py')
        try:
            scriptContent = requests.get(self.links['ScriptDownload']).text
            try:
                os.remove(scriptPath)
            except FileNotFoundError:
                pass
            with open(scriptPath, 'w') as script:
                script.write(scriptContent)
            return True
        except Exception as e:
            return False

    def __downloadModule(self):
        tmPath = self.getTmPath()
        modulePath = tmPath.replace(
            'TerminalManager.exe', 'TMRemote/Scripts/TMRLogger.pyc')
        try:
            moduleContent = requests.get(self.links['ModuleDownload']).content
            try:
                os.remove(modulePath)
            except FileNotFoundError:
                pass
            with open(modulePath, 'wb+') as moduleFile:
                moduleFile.write(moduleContent)
            return True
        except Exception as e:
            return False

    def run(self):
        while True:
            self.__checkTerminalScripts()
            self.sleep(self.sleep_time)
