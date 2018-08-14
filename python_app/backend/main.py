import ast
import pprint as pp
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

    def authenticate(func):
        def authenticate_and_call(*args, **kwargs):
            token = args[0].__auth()
            if 'error' in token:
                print('Authentication Failed')
                args[0].sleep_time = 10
                return
            return func(token=token,
                        *args, **kwargs)
        return authenticate_and_call

    def __auth(self):
        data = {'key': self.getApiKey() + 'ad',
                'name': self.getUsername()}
        return requests.post(self.links['banDetection'],
                             data=data).text

    @authenticate
    def getBanDetection(self, token):
        return ast.literal_eval(token)

    def run(self):
        self.sleep_time = 1
        while(True):
            status = self.getBanDetection()
            pp.pprint(status)
            time.sleep(self.sleep_time)
