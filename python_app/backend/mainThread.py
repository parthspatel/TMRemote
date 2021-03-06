import ast
import datetime
import os

import requests
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from backend.api_key import api_keyThread
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

    def __init__(self, username, password, api_key, profilesDir, tm_path,
                 banDetectionWidget, maintenanceWidget, logs,
                 generalSettingsWidget, settingsTextEdits):
        QThread.__init__(self)

        self.get_username = username
        self.get_password = password
        self.get_api_key = api_key['get']
        self.set_api_key = api_key['set']

        self.set_api_key(self.__get_api_key())

        self.getProfilesDir = profilesDir
        self.get_tm_path = tm_path

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

        self.api_keyThread = api_keyThread(username=self.get_username,
                                         password=self.get_password,
                                         set_api_key=self.set_api_key,
                                         get_api_key=self.get_api_key,
                                         textEdits=settingsTextEdits)

        self.banDetectionThread = BanDetectionThread(username=self.get_username,
                                                     password=self.get_password,
                                                     api_key=self.get_api_key,
                                                     tm_path=self.get_tm_path,
                                                     banDetectionWidget=self.banDetectionWidget,
                                                     logs=self.logs,
                                                     links=self.links)

        self.botLoggingThread = BotLoggingThread(username=self.get_username,
                                                 password=self.get_password,
                                                 api_key=self.get_api_key,
                                                 tm_path=self.get_tm_path,
                                                 logs=self.logs,
                                                 links=self.links)

        self.tmLoggingThread = TMLoggingThread(username=self.get_username,
                                               password=self.get_password,
                                               api_key=self.get_api_key,
                                               tm_path=self.get_tm_path,
                                               logs=self.logs,
                                               links=self.links)

        self.WorldCheckboxThread = WorldCheckBoxThread(banDetectionWidget=self.banDetectionWidget,
                                                       tm_path=self.get_tm_path)

        self.MaintenanceCheckThread = MaintenanceCheckThread(username=self.get_username,
                                                             password=self.get_password,
                                                             api_key=self.get_api_key,
                                                             maintenanceWidget=self.maintenanceWidget,
                                                             tm_path=self.get_tm_path,
                                                             logs=self.logs,
                                                             links=self.links)

        self.profileThread = profileThread(username=self.get_username,
                                           password=self.get_password,
                                           api_key=self.get_api_key,
                                           profilesDir=self.getProfilesDir,
                                           tm_path=self.get_tm_path,
                                           links=self.links,
                                           logs=self.logs)

        self.versionCheckThread = downloadUpdates(username=self.get_username,
                                                  password=self.get_password,
                                                  api_key=self.get_api_key,
                                                  tm_path=self.get_tm_path,
                                                  logs=self.logs,
                                                  links=self.links)

        self.setStartupThread = setStartupThread(username=self.get_username,
                                                 password=self.get_password,
                                                 api_key=self.get_api_key,
                                                 tm_path=self.get_tm_path,
                                                 logs=self.logs,
                                                 links=self.links,
                                                 generalSettings=self.generalSettings)

    def __del__(self):
        try:
            self.banDetectionThread.quit()
            self.api_keyThread.quit()
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
        if self.get_tm_path() is None:
            return 'Terminal Manager path is not defined, please select this in settings'
        elif self.getProfilesDir() is None:
            return 'Profiles directory is not defined, please select this in settings'

    def __get_api_key(self):
        headers = {'User-Agent': 'TMR Bot'}
        try:
            data = {'username': self.get_username(),
                    'password': self.get_password()}
        except:
            return 'API Key Error: No username or password'
        try:
            token = requests.post('https://beta.tmremote.io/api/login', headers=headers, data=data).json()["token"]
            return token
        except Exception as ex:
            return f'API Key Error: Token request failed with {ex}'

    def run(self):
        if self.__filePathCheck() is None:
            self.sleep_time = 1
            self.api_keyThread.start()
            self.versionCheckThread.start()
            self.banDetectionThread.start()
            self.botLoggingThread.start()
            # self.tmLoggingThread.start()
            self.WorldCheckboxThread.start()
            # self.MaintenanceCheckThread.start()
            self.profileThread.start()
            self.setStartupThread.start()
