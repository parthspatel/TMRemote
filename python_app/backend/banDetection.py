import ast
import datetime
import pickle
import time

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from backend.auth import Auth
from backend.log import Log


class BanDetectionThread(QThread, ):
    def __init__(self, username, password, apikey, tmPath, logs, links):
        QThread.__init__(self)
        self.getUsername = username
        self.getPassword = password
        self.getApiKey = apikey

        self.getTmPath = tmPath

        self.logs = logs
        self.links = links

        self.sleep_time = 10
        self.prevBanDetection = {}

    def __del__(self):
        self.wait()

    def __getTMRemoteFolder(self):
        return self.getTmPath().split('TerminalManager.exe')[0] + 'TMRemote'

    @Auth.authenticate
    def __getBanDetection(self, token):
        return ast.literal_eval(token)

    @Log.log
    def parseBanDetection(self):
        status = self.__getBanDetection()
        if dict is not type(status):
            return status
        gm_status = []

        for world in status:
            if 'time' in world:
                continue
            if status[world] != self.prevBanDetection.get(world):
                gm_status.append(f'{world}:{status[world]}')
                self.prevBanDetection[world] = status[world]

        if not self.prevBanDetection:
            self.prevBanDetection = status

        try:
            with open(self.__getTMRemoteFolder + '/temp/banDetectStatus', 'wb') as file:
                pickle.dump(str(status), file)
        except:
            return 'Could not access TMRemote folder'

        return gm_status

    def run(self):
        self.parseBanDetection()
        time.sleep(self.sleep_time)
