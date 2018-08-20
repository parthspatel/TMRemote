import os
import pickle
import sys
import urllib

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
        self.getApiKey = apikey

        self.getTmPath = tmPath
        self.logs = logs

        self.links = links

        self.sleep_time = 600

    def __del__(self):
        self.wait()

    def __getCurrentScriptVersion(self):
        data = {'key': self.getApiKey(),
                'name': self.getUsername()}
        scriptVersion = int(requests.post(self.links['ScriptVersion'], data=data))
        moduleVersion = int(requests.post(self.links['ModuleVersion'], data=data))
        versionDict = {'scriptVersion': scriptVersion,
                       'moduleVersion': moduleVersion}
        return versionDict

    @Log.log
    @Auth.authenticate(level='basic')
    def __checkTerminalScripts(self):
        tmPath = self.getTmPath()
        scriptsFolder = tmPath + '/TMRemote/Scripts'
        tmRemoteFolder = tmPath + '/TMRemote'
        if not os.path.isdir(tmRemoteFolder):
            os.mkdir(tmRemoteFolder)
        if not os.path.isdir(scriptsFolder):
            os.mkdir(scriptsFolder)
        self.__downloadScript(path=scriptsFolder)
        self.__downloadModule(path=scriptsFolder)


    def __downloadScript(self):
        data = {'key': self.getApiKey(),
                'name': self.getUsername()}
        try:
            urllib.urlretrieve(self.links['ScriptDownload'], scriptsFolder + '/Logger.py')
            return True
        except:
            return False

    def __downloadModule(self):
        data = {'key': self.getApiKey(),
                'name': self.getUsername()}
        try:
            urllib.urlretrieve(self.links['ModuleDownload'], scriptsFolder + '/TMRLogger.pyc')
            return True
        except:
            return False


    def run(self):
        while True:
            self.__checkTerminalScripts()
            self.sleep(self.sleep_time)
