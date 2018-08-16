import ast
import datetime
import os
import pickle
import time

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

        self.sleep_time = 10

    def __del__(self):
        self.wait()

    def __getTMRemoteFolder(self):
        return self.getTmPath().split('TerminalManager.exe')[0] + 'TMRemote'

    @Auth.authenticate
    @Log.log
    def __PostLogs(self, logs):
        PostedPreviously = []
        if type(logs) is not list:
            if logs:
                pass  # incorrect logs type
            return
        toPost = {}
        count = 0
        for index in range(len(logs)):
            try:
                if not 'disconnect' in logs[index]:
                    if not logs[index]['IGN'] in PostedPreviously:
                        data = {'key': self.getApiKey(),
                                'name': self.getUsername(),
                                # 'HWID': self.HWID(),
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
                            # 'HWID': self.HWID(),
                            'server': 'GMS',
                            'disconnect': logs[index]['disconnect']}
            except Exception as e:
                return e
        if count > 0:
            response = requests.post(self.links['botLogs'], data=toPost)
            return f'Posted logs of {count} bots'

    # Get the log values and returns data
    @Log.log
    def __GetLogs(self):
        try:
            with open(self.__getTMRemoteFolder() + '/temp/logs', 'rb') as file:
                data = []
                while True:
                    try:
                        data.append(pickle.load(file))
                    except EOFError:
                        break
                    except pickle.UnpicklingError:
                        break
            os.remove(self.__getTMRemoteFolder() + '/temp/logs')
            return data
        except FileNotFoundError:
            return None
        except PermissionError:
            return 'TMRemote does not have permissions to read logs'

    def run(self):
        print('running BotLogs')
        while True:
            self.__PostLogs(logs=self.__GetLogs())
            print('ran botlogs')
            time.sleep(self.sleep_time)
