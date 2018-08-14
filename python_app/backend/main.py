import time

import requests
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MainThread(QThread):

    def __init__(self, username, password, apikey, profilesDir, tmPath, logs):
        QThread.__init__(self)

        self.getUsername = username
        self.getPassword = password
        self.getApiKey = apikey

        self.getProfilesDir = profilesDir
        self.getTmPath = tmPath

        self.logs = logs

        self.links = {'api': 'https://tmremote.io/api/v1/activity',
                      'banDetection': 'https://tmremote.io/api/v1/gm/status',
                      'banPost': '',
                      'tmLog': ''}

    def __del__(self):
        self.wait()

    def authenticate(self):
        data = {'key': self.getApiKey(),
                'name': self.getUsername()}
        return requests.post(self.links['banDetection'], data=data).text

    def run(self):
        while(True):
            response = self.authenticate()
            print(response)
