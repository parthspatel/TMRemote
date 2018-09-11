
import ast
import os
import pickle

import requests
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from backend.auth import Auth
from backend.log import Log


class apiKeyThread(QThread):
    def __init__(self, username, password, setApiKey, getApiKey):
        QThread.__init__(self)
        self.getUsername = username
        self.getPassword = password

        self.setApiKey = setApiKey
        self.getApiKey = getApiKey

        self.sleep_time = 60
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
            return token
        except Exception as ex:
            return f'API Key Error: Token request failed with {ex}'

    def run(self):
        num_failed = 0
        apiKey = self.getApiKey()
        while True:

            if not bool(apiKey):
                apiKey = self.__getApiKey()

            if 'error' in apiKey.lower():
                self.sleep_time = 600  # 10mins
                num_failed += 1

                if 5 < num_failed:
                    self.sleep_time = 3600  # 1 hour

                elif 10 < num_failed:
                    num_failed = 0

                apiKey = self.__getApiKey()
            else:
                self.sleep_time = 3600
                self.setApiKey(apiKey)

            self.sleep(self.sleep_time)
