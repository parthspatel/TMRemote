
import ast
import os
from copy import deepcopy

import requests
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from backend.auth import Auth
from backend.log import Log


class apiKeyThread(QThread):
    def __init__(self, username, password, setApiKey, getApiKey, textEdits):
        QThread.__init__(self)
        self.getUsername = username
        self.getPassword = password

        self.setApiKey = setApiKey
        self.getApiKey = getApiKey

        self.textEdits = textEdits

        self.sleep_time = 60
        self.sleep_time_const = self.sleep_time

    def __getApiKey(self):
        headers = {'User-Agent': 'TMR Bot'}
        try:
            if self.getUsername() is None or self.getPassword() is None:
                # Otherwise it will never except, it would just return None
                raise Exception('No username or password')
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
        # apiKey = self.getApiKey()
        apiKey = self.__getApiKey()
        old_creds = {'username': self.getUsername(),
                     'password': self.getPassword()}

        while True:
            creds = {'username': self.getUsername(),
                     'password': self.getPassword()}

            if not isDictEquals(creds, old_creds):
                apiKey = self.__getApiKey()
                old_creds = deepcopy(creds)

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


def isDictEquals(d1: dict, d2: dict, ignore_keys: dict = {}):
    ignored = set(ignore_keys)
    for k1, v1 in d1.items():
        if k1 not in ignored and (k1 not in d2 or d2[k1] != v1):
            return False
    for k2, v2 in d2.items():
        if k2 not in ignored and k2 not in d1:
            return False
    return True
