import time

import requests
import ast
import pickle
import os

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MainThread(QThread):

    def __init__(self, username, password, apikey, profilesDir, tmPath, logs, banDetect):
        QThread.__init__(self)

        self.getUsername = username
        self.getPassword = password
        self.getApiKey = apikey

        self.getProfilesDir = profilesDir
        self.getTmPath = tmPath
        self.filePaths = {'TerminalManagerFolder':''}

        self.baseData = {}

        self.logs = logs

        self.banDetect = banDetect

        self.links = {'botLogs': 'https://tmremote.io/api/v1/activity',
                      'banDetection': 'https://tmremote.io/api/v1/gm/status',
                      'banPost': '',
                      'tmLog': ''}

    def __del__(self):
        self.wait()

    def __UpdateVariables(self):
        self.baseData = {'key': self.getApiKey(),
                         'name':self.getUsername()}
        self.filePaths['TerminalManagerFolder'] = self.getTmPath().split('TerminalManager.exe')[0]

    def authenticate(self):
        return requests.post(self.links['botLogs'], data=self.baseData).text

    def __GetGMLogs(self):
        if self.banDetect.banDetectionCheckBox.isChecked():
            response = requests.post(self.links['banDetection'], data=self.baseData).text
            dictionaryResponse = ast.literal_eval(response.lower())
            pickleData = {}
            for world in self.banDetect.worldCheckBoxes:
                worldValue = dictionaryResponse[world]
                pickleData[world] = worldValue
                self.banDetect.worldCheckBoxes[world].setState(worldValue)
            try:
                os.remove(self.filePaths['TerminalManagerFolder'] + '/TMRemote/GMStatus')
            except FileNotFoundError:
                pass
            with open(self.filePaths['TerminalManagerFolder'] + '/TMRemote/GMStatus', 'wb') as pickleFile:
                pickle.dump(pickleData, pickleFile)
        else: return

    def run(self):
        while(True):
            self.__UpdateVariables()
            response = self.authenticate()
            if not response == 'success':
                continue
            self.__GetGMLogs()
