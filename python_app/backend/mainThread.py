import ast
import datetime
import os

import requests
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from backend.auth import Auth
from backend.banDetection import BanDetectionThread
from backend.botLogging import BotLoggingThread
from backend.tmLogging import TMLoggingThread
from backend.worldCheckboxStatus import WorldCheckBoxThread


def getCurrentPath():
    if getattr(sys, 'frozen', False):
        dir = os.path.dirname(sys.executable)
    else:
        dir = os.path.dirname(os.path.realpath(__file__))
    return dir


class MainThread(QThread):

    def __init__(self, username, password, apikey, profilesDir, tmPath, banDetectionWidget, logs):
        QThread.__init__(self)

        self.getUsername = username
        self.getPassword = password
        self.getApiKey = apikey

        self.getProfilesDir = profilesDir
        self.getTmPath = tmPath

        self.banDetectionWidget = banDetectionWidget
        self.worldCheckBoxes = self.banDetectionWidget.worldCheckBoxes

        self.logs = logs

        self.links = {'botLogs': 'https://tmremote.io/api/v1/activity',
                      'banDetection': 'https://tmremote.io/api/v1/gm/status',
                      'banPost': '',
                      'tmLog': '',
                      'ExeDownload': '',
                      'VersionCheck': '',
                      'MaintenanceCheck': ''}

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

    def __del__(self):
        self.banDetectionThread.quit()
        self.botLoggingThread.quit()
        self.tmLoggingThread.quit()
        self.WorldCheckboxThread.quit()
        self.wait()

    def run(self):
        self.sleep_time = 1

        self.banDetectionThread.start()
        self.botLoggingThread.start()
        self.tmLoggingThread.start()
        self.WorldCheckboxThread.start()