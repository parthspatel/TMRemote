import os
import pickle

import json
import requests

from PyQt5.QtCore import QThread

from backend.auth import Auth
from backend.log import Log


class BotLoggingThread(QThread):
    def __init__(self, username, password, api_key, tm_path, logs, links):
        QThread.__init__(self)
        self.get_username = username
        self.get_password = password
        self.api_key = api_key

        self.get_tm_path = tm_path

        self.logs = logs
        self.links = links

        self.sleep_time = 10
        self.sleep_time_const = self.sleep_time

        self.HWID = Auth.HardwareID().asStr()  # Error

    def __del__(self):
        self.wait()

    def get_tmremote_folder(self):
        return self.get_tm_path().split('TerminalManager.exe')[0] + 'TMRemote'

    @Log.log
    def __PostLogs(self, logs, token=None):
        postedPreviously = []
        headers = {'User-Agent': 'TMR Bot',
                   'Authorization':'Bearer {}'.format(self.api_key())}
        if type(logs) is not list:
            return logs
        to_post = []
        count = 0
        for index in range(len(logs)):
            try:
                if 'disconnect' in logs[index]:
                    continue
                
                if logs[index]['IGN'] in postedPreviously:
                    continue

                data = {'user_id':self.get_username(),
                        'char_id':logs[index]['CharID'],
                        'char_name':logs[index]['IGN'],
                        'world_id':logs[index]['World'],
                        'channel':logs[index]['Channel'],
                        'level':logs[index]['Level'],
                        'mesos':logs[index]['Meso'],
                        'map_id':logs[index]['mapID']}
                count += 1
                to_post.append(data)
                postedPreviously.append(logs[index]['IGN'])

            except Exception as e:
                return e
        if not count:
            return
        data = {'bot_logs':to_post}
        try:
            requests.post(self.links['botLogs'], headers=headers,json=data)
        except Exception as ex:
            return f'No Internet: {ex}'

    def __getLogs(self):
        try:
            if not self.get_tmremote_folder():
                return
            with open(self.get_tmremote_folder() + '/temp/logs', 'rb') as file:
                data = []
                while True:
                    try:
                        data.append(pickle.load(file))
                    except BaseException:
                        break
            os.remove(self.get_tmremote_folder() + '/temp/logs')
            return data
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
