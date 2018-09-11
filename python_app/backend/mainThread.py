import ast
import datetime
import os

import requests
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from backend.apiKey import apiKeyThread
from backend.auth import Auth
from backend.banDetection import BanDetectionThread
from backend.botLogging import BotLoggingThread
from backend.downloadScripts import downloadUpdates
from backend.log import Log
from backend.maintenance import MaintenanceCheckThread
from backend.profileManager import profileThread
from backend.setStartup import setStartupThread
from backend.tmLogging import TMLoggingThread
from backend.worldCheckboxStatus import WorldCheckBoxThread


def getCurrentPath():
    if getattr(sys, 'frozen', False):
        dir = os.path.dirname(sys.executable)
    else:
        dir = os.path.dirname(os.path.realpath(__file__))
    return dir


class MainThread(QThread):

    def __init__(self, username, password, apikey, profilesDir, tmPath,
                 banDetectionWidget, maintenanceWidget, logs,
                 generalSettingsWidget, settingsTextEdits):
        QThread.__init__(self)

        self.getUsername = username
        self.getPassword = password
        self.getApiKey = apikey['get']
        self.setApiKey = apikey['set']

        self.setApiKey(self.__getApiKey())

        self.getProfilesDir = profilesDir
        self.getTmPath = tmPath

        self.banDetectionWidget = banDetectionWidget
        self.worldCheckBoxes = self.banDetectionWidget.worldCheckBoxes

        self.generalSettings = generalSettingsWidget

        self.maintenanceWidget = maintenanceWidget

        self.logs = logs

        self.links = {'logIn': 'https://beta.tmremote.io/api/login',
                      'botLogs': 'https://beta.tmremote.io/api/bots/log',
                      'banDetection': 'https://beta.tmremote.io/api/gm/status',
                      'banPost': '',
                      'tmLog': '',
                      'MaintenanceCheck': '',
                      'ScriptDownload': 'https://mehodin.com/i/Logger.py',
                      'ModuleDownload': 'https://mehodin.com/i/TMRLogger.pyc',
                      'ScriptVersion': 'https://mehodin.com/scriptVersion.html',
                      'ModuleVersion': 'https://mehodin.com/moduleVersion.html'}

        self.apiKeyThread = apiKeyThread(username=self.getUsername,
                                         password=self.getPassword,
                                         setApiKey=self.setApiKey,
                                         getApiKey=self.getApiKey,
                                         textEdits=settingsTextEdits)

        self.banDetectionThread = BanDetectionThread(username=self.getUsername,
                                                     password=self.getPassword,
                                                     apikey=self.getApiKey,
                                                     tmPath=self.getTmPath,
                                                     banDetectionWidget=self.banDetectionWidget,
                                                     logs=self.logs,
                                                     links=self.links)

        self.botLoggingThread = BotLoggingThread(username=self.getUsername,
                                                 password=self.getPassword,
                                                 apikey=self.getApiKey,
                                                 tmPath=self.getTmPath,
                                                 logs=self.logs,
                                                 links=self.links)

        self.tmLoggingThread = TMLoggingThread(username=self.getUsername,
                                               password=self.getPassword,
                                               apikey=self.getApiKey,
                                               tmPath=self.getTmPath,
                                               logs=self.logs,
                                               links=self.links)

        self.WorldCheckboxThread = WorldCheckBoxThread(banDetectionWidget=self.banDetectionWidget,
                                                       tmPath=self.getTmPath)

        self.MaintenanceCheckThread = MaintenanceCheckThread(username=self.getUsername,
                                                             password=self.getPassword,
                                                             apikey=self.getApiKey,
                                                             maintenanceWidget=self.maintenanceWidget,
                                                             tmPath=self.getTmPath,
                                                             logs=self.logs,
                                                             links=self.links)

        self.profileThread = profileThread(username=self.getUsername,
                                           password=self.getPassword,
                                           apikey=self.getApiKey,
                                           profilesDir=self.getProfilesDir,
                                           tmPath=self.getTmPath,
                                           links=self.links,
                                           logs=self.logs)

        self.versionCheckThread = downloadUpdates(username=self.getUsername,
                                                  password=self.getPassword,
                                                  apikey=self.getApiKey,
                                                  tmPath=self.getTmPath,
                                                  logs=self.logs,
                                                  links=self.links)

        self.setStartupThread = setStartupThread(username=self.getUsername,
                                                 password=self.getPassword,
                                                 apikey=self.getApiKey,
                                                 tmPath=self.getTmPath,
                                                 logs=self.logs,
                                                 links=self.links,
                                                 generalSettings=self.generalSettings)

    def __del__(self):
        try:
            self.banDetectionThread.quit()
            self.apiKeyThread.quit()
            self.botLoggingThread.quit()
            self.tmLoggingThread.quit()
            self.WorldCheckboxThread.quit()
            self.MaintenanceCheckThread.quit()
            self.profileThread.quit()
            self.versionCheckThread.quit()
            self.setStartupThread.quit()
        except:
            pass
        finally:
            self.wait()

    @Log.log
    def __filePathCheck(self):
        if self.getTmPath() is None:
            return 'Terminal Manager path is not defined, please select this in settings'
        elif self.getProfilesDir() is None:
            return 'Profiles directory is not defined, please select this in settings'

    def __getApiKey(self):
        headers = {'User-Agent': 'TMR Bot'}
        try:
            data = {'username': self.getUsername(),
                    'password': self.getPassword()}
        except:
            return 'API Key Error: No username or password'
        try:
            token = ast.literal_eval(requests.post(
                'https://beta.tmremote.io/api/login', headers=headers, data=data).text)['token']
            return token
        except Exception as ex:
            return f'API Key Error: Token request failed with {ex}'

    def run(self):
        if self.__filePathCheck() is None:
            self.sleep_time = 1
            self.apiKeyThread.start()
            self.versionCheckThread.start()
            self.banDetectionThread.start()
            self.botLoggingThread.start()
            # self.tmLoggingThread.start()
            self.WorldCheckboxThread.start()
            # self.MaintenanceCheckThread.start()
            self.profileThread.start()
            self.setStartupThread.start()
