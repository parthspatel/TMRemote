
import ast
import os
from copy import deepcopy

import requests
from PyQt5.QtCore import QThread

from backend.auth import Auth
from backend.log import Log


class api_keyThread(QThread):
    def __init__(self, username, password, set_api_key, get_api_key, textEdits):
        QThread.__init__(self)
        self.get_username = username
        self.get_password = password

        self.set_api_key = set_api_key
        self.get_api_key = get_api_key

        self.textEdits = textEdits

        self.sleep_time = 60
        self.sleep_time_const = self.sleep_time

    def __get_api_key(self):
        headers = {'User-Agent': 'TMR Bot'}
        try:
            if self.get_username() is None or self.get_password() is None:
                # Otherwise it will never except, it would just return None
                raise Exception('No username or password')
            data = {'username': self.get_username(),
                    'password': self.get_password()}
        except BaseException:
            return 'API Key Error: No username or password'
        try:
            token = requests.post(
                'https://beta.tmremote.io/api/login',
                headers=headers,
                data=data).json()["token"]
            return token
        except Exception as ex:
            return f'API Key Error: Token request failed with {ex}'

    def run(self):
        num_failed = 0
        # api_key = self.get_api_key()
        api_key = self.__get_api_key()
        old_creds = {'username': self.get_username(),
                     'password': self.get_password()}

        while True:
            creds = {'username': self.get_username(),
                     'password': self.get_password()}

            if not isDictEquals(creds, old_creds):
                api_key = self.__get_api_key()
                old_creds = deepcopy(creds)

            if not bool(api_key):
                api_key = self.__get_api_key()

            if 'error' in api_key.lower():
                self.sleep_time = 600  # 10mins
                num_failed += 1

                if 5 < num_failed:
                    self.sleep_time = 3600  # 1 hour

                elif 10 < num_failed:
                    num_failed = 0

                api_key = self.__get_api_key()

            else:
                self.sleep_time = 3600
                self.set_api_key(api_key)

            self.sleep(self.sleep_time)


def isDictEquals(d1: dict, d2: dict, ignore_keys: dict = {}):
    ignored = set(ignore_keys)
    for k1, v1 in d1.items():
        if k1 not in ignored and (k1 not in d2 or d2[k1] != v1):
            return False
    for k2, _ in d2.items():
        if k2 not in ignored and k2 not in d1:
            return False
    return True
