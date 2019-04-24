import os
import pickle
import re
import sys

import requests
from PyQt5.QtCore import QThread

from backend.auth import Auth
from backend.log import Log

class downloadUpdates(QThread):
    def __init__(self, username, password, api_key, tm_path, logs, links):
        QThread.__init__(self)
        self.get_username = username
        self.get_password = password
        self.api_key = api_key

        self.get_tm_path = tm_path
        self.logs = logs

        self.links = links

        self.sleep_time = 60
        self.sleep_time_const = 10

    def __del__(self):
        self.wait()

    def __checkTerminalScripts(self):
        self.__downloadModule()
        self.__downloadScript()

    def __downloadScript(self, token=None):
        tm_path = self.get_tm_path()
        scriptPath = tm_path.replace(
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
        except Exception:
            return False

    def __downloadModule(self):
        tm_path = self.get_tm_path()
        modulePath = tm_path.replace(
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
        except Exception:
            return False

    def run(self):
        while True:
            self.__checkTerminalScripts()
            self.sleep(self.sleep_time)
