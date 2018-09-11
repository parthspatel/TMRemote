import os
import pickle

import json
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
        self.apiKey = apikey

        self.getTmPath = tmPath

        self.logs = logs
        self.links = links

        self.sleep_time = 10
        self.sleep_time_const = self.sleep_time

        self.HWID = Auth.HardwareID().asStr()  # Error

    def __del__(self):
        self.wait()

    def __getTMRemoteFolder(self):
        return self.getTmPath().split('TerminalManager.exe')[0] + 'TMRemote'

    @Log.log
    def __PostLogs(self, logs, token=None):
        postedPreviously = []
        headers = {'User-Agent': 'TMR Bot',
                   'Authorization':'Bearer {}'.format(self.apiKey())}
        if type(logs) is not list:
            return logs
        toPost = []
        count = 0
        for index in range(len(logs)):
            try:
                if not 'disconnect' in logs[index]:
                    if not logs[index]['IGN'] in postedPreviously:
                        data = {'user_id':self.getUsername(),
                        		'char_id':logs[index]['CharID'],
                        		'char_name':logs[index]['IGN'],
                        		'world_id':logs[index]['World'],
                        		'channel':logs[index]['Channel'],
                        		'level':logs[index]['Level'],
                        		'mesos':logs[index]['Meso'],
                        		'map_id':logs[index]['mapID']}
                        count += 1
                        toPost.append(data)
                        postedPreviously.append(logs[index]['IGN'])
                else:
                    continue
                    data = {'key': self.apiKey,
                            'name': self.getUsername(),
                            'HWID': self.HWID,
                            'server': 'GMS',
                            'disconnect': logs[index]['disconnect']}
            except Exception as e:
                return e
        if count > 0:
            data = {'bot_logs':toPost}
            try:
                response = requests.post(self.links['botLogs'], headers=headers,json=data)
            except Exception as ex:
                return f'No Internet: {ex}'

    def __getLogs(self):
        try:
            if self.__getTMRemoteFolder():
                with open(self.__getTMRemoteFolder() + '/temp/logs', 'rb') as file:
                    data = []
                    while True:
                        try:
                            data.append(pickle.load(file))
                        except Exception as ex:
                            break
                os.remove(self.__getTMRemoteFolder() + '/temp/logs')
                return data
            else:
                return
        except FileNotFoundError:
            pass
        except PermissionError:
            pass
        except ValueError:
            pass

    def run(self):
        while True:
            self.__PostLogs(logs=self.__getLogs())
            self.sleep(self.sleep_time)
