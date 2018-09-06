import os
import pickle
import sys
import re

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

        self.versions = {}

        self.links = links

        self.sleep_time = 10
        self.sleep_time_const = 10

    def __del__(self):
        self.wait()

    def __getCurrentScriptVersion(self):
        data = {'key': self.apiKey(),
                'name': self.getUsername()}
        scriptVersion = requests.get(
            self.links['ScriptVersion']).text
        moduleVersion = requests.get(
            self.links['ModuleVersion']).text
        scriptVersion = re.search('<p>(.*)</p>', scriptVersion).group(1)
        moduleVersion = re.search('<p>(.*)</p>', moduleVersion).group(1)
        versionDict = {'scriptVersion': scriptVersion,
                       'moduleVersion': moduleVersion}
        self.versions = versionDict
        return versionDict

    @Log.log
    def __checkTerminalScripts(self, token):
        tmPath = self.getTmPath().split('TerminalManager.exe')[0]
        scriptsFolder = tmPath + 'TMRemote/Scripts'
        tmRemoteFolder = tmPath + 'TMRemote'
        if not os.path.isdir(tmRemoteFolder):
            os.mkdir(tmRemoteFolder)
        if not os.path.isdir(scriptsFolder):
            os.mkdir(scriptsFolder)
        if not scriptsFolder in sys.path:
            sys.path.append(scriptsFolder)
        try:
            import TMRLogger
            moduleVersion = TMRLogger.versionCheck().version
        except ModuleNotFoundError as E:
            self.__downloadModule()
            return f'Downloaded Module to folder: {scriptsFolder}'
        try:
            import Logger
            scriptVersion = TMRLogger.versionCheck().version
        except ModuleNotFoundError:
            self.__downloadScript()
            return f'Downloaded Script to folder: {scriptsFolder}'
        newVersions = {'scriptVersion':1.0, 'moduleVersion':1.0}#self.__getCurrentScriptVersion()
        if scriptVersion != str(newVersions['scriptVersion']):
            self.__downloadScript()
            return f'Downloaded Script to folder: {scriptsFolder}'
        if moduleVersion != str(newVersions['moduleVersion']):
            self.__downloadModule()
            return f'Downloaded Module to folder: {scriptsFolder}'

    @Auth.authenticate(level='basic')
    def __downloadScript(self):
        tmPath = self.getTmPath()
        scriptPath = tmPath.replace('TerminalManager.exe','TMRemote/Scripts/Logger.py')
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

    @Auth.authenticate(level='basic')
    def __downloadModule(self):
        tmPath = self.getTmPath()
        modulePath = tmPath.replace('TerminalManager.exe','TMRemote/Scripts/TMRLogger.pyc')
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
            # self.__checkTerminalScripts()
            self.sleep(self.sleep_time)
