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

        self.sleep_time = 30

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
        if not scriptsFolder in sys.path:
            sys.path.append(scriptsFolder)
        import TMRLogger
        import Logger
        if not os.path.isdir(tmRemoteFolder):
            try:
                os.mkdir(tmRemoteFolder)
                return f'Successfully created folder {tmRemoteFolder}'
            except:
                return f'Failed to create folder {tmRemoteFolder}'
        if not os.path.isdir(scriptsFolder):
            try:
                os.mkdir(scriptsFolder)
                return f'Successfully created folder {scriptsFolder}'
            except:
                return f'Failed to create folder {scriptsFolder}'
        if not os.path.isfile(scriptsFolder + '/Logger.py'):
            if self.__getCurrentScriptVersion()['scriptVersion'] < Logger.versionCheck().version:
                if self.__downloadScript(path=scriptsFolder):
                    return f'Successfully downloaded script to {scriptsFolder}'
                else:
                    return f'Failed to download script to {scriptsFolder}'
        if not os.path.isfile(scriptsFolder + 'TMRLogger.pyc'):
            if self.__getCurrentScriptVersion()['moduleVersion'] < TMRLogger.versionCheck().version:
                if self.__downloadModule(path=scriptsFolder):
                    return f'Successfully downloaded module to {scriptsFolder}'
                else:
                    return f'Failed to download module to {scriptsFolder}'

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
