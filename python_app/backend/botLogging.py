import os
import pickle

import requests
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from backend.auth import Auth
from backend.log import Log


class BotLoggingThread(QThread):
    def __init__(self, username, password, apikey, tmPath, logs, links):
        QThread.__init__(self)
        self.getUsername = username
        self.getPassword = password
        self.getApiKey = apikey

        self.getTmPath = tmPath

        self.logs = logs
        self.links = links

        self.sleep_time = 30
        self.sleep_time_const = self.sleep_time

        self.HWID = Auth.HardwareID().asStr()  # Error

    def __del__(self):
        self.wait()

    def __getTMRemoteFolder(self):
        return self.getTmPath().split('TerminalManager.exe')[0] + 'TMRemote'

    @Auth.authenticate(level='basic')
    @Log.log
    def __PostLogs(self, logs, token):
        PostedPreviously = []
        if type(logs) is not list:
            return logs
        toPost = {}
        count = 0
        for index in range(len(logs)):
            try:
                if not 'disconnect' in logs[index]:
                    if not logs[index]['IGN'] in PostedPreviously:
                        data = {'key': self.getApiKey(),
                                'name': self.getUsername(),
                                'HWID': self.HWID,
                                'server': 'GMS',
                                'world_id': logs[index]['World'],
                                'channel': logs[index]['Channel'],
                                'character_id': logs[index]['CharID'],
                                'character': logs[index]['IGN'],
                                'level': logs[index]['Level'],
                                'mesos': logs[index]['Meso'],
                                'nodes': logs[index]['UntradableNodes'] + logs[index]['TradableNodes']}
                        count += 1
                        toPost[str(count)] = data
                        PreviouslyPosted.append(logs[index]['IGN'])
                else:
                    continue
                    data = {'key': self.getApiKey(),
                            'name': self.getUsername(),
                            'HWID': self.HWID,
                            'server': 'GMS',
                            'disconnect': logs[index]['disconnect']}
            except Exception as e:
                return e
        if count > 0:
            try:
                response = requests.post(self.links['botLogs'], data=toPost)
            except Exception as ex:
                return f'No Internet: {ex}'
            return f'Posted logs of {count} bots'

    # Get the log values and returns data
    def __getLogs(self):
        try:
            if self.__getTMRemoteFolder():
                with open(self.__getTMRemoteFolder() + '/temp/logs', 'rb') as file:
                    data = []
                    while True:
                        try:
                            data.append(pickle.load(file))
                        except Exception as ex:
                            return ex
                os.remove(self.__getTMRemoteFolder() + '/temp/logs')
                return data
            else:
                return
        except FileNotFoundError:
            return 'No logs found'
        except PermissionError:
            return 'TMRemote does not have permissions to read logs'

    def run(self):
        while True:
            self.__PostLogs(logs=self.__getLogs())
            self.sleep(self.sleep_time)
