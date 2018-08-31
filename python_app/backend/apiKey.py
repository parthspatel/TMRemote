import ast
import os
import pickle

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from backend.auth import Auth
from backend.log import Log


class apiKeyThread(QThread):
    def __init__(self, username, password):
        QThread.__init__(self)
        self.getUsername = username
        self.getPassword = password

        self.sleep_time = 5
        self.sleep_time_const = self.sleep_time

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
        except:
            pass
        return token

    def run(self):
        while True:
            self.__getApiKey()
            self.sleep(self.sleep_time)
