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


class BanDetectionThread(QThread, ):
    def __init__(self, username, password, apikey, tmPath, worldCheckBoxes, logs, links):
        QThread.__init__(self)
        self.getUsername = username
        self.getPassword = password
        self.getApiKey = apikey

        self.getTmPath = tmPath

        self.worldCheckBoxes = worldCheckBoxes

        self.logs = logs
        self.links = links

        self.sleep_time = 10
        self.prevBanDetection = {}

    def __del__(self):

        self.__removeTempFiles(self.__getTMRemoteFolder() + '/temp/banDetectStatus')
        self.wait()

    def __removeTempFiles(self, file):
        try:
            os.remove(file)
        except Exception as ex:
            print(ex)

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
                worldKey = world
                if world.lower() == 'reboot':
                    worldKey = 'RebootNA'
                self.worldCheckBoxes[worldKey.lower()].setState(status[world])

                gm_status.append(f'BD Status: {status[world]} in {world}')
                self.prevBanDetection[world] = status[world]

        try:
            if not os.path.exists(self.__getTMRemoteFolder() + '/temp'):
                os.makedirs(self.__getTMRemoteFolder() + '/temp')
            with open(self.__getTMRemoteFolder() + '/temp/banDetectStatus', 'wb+') as file:
                pickle.dump(str(status), file)
        except Exception as ex:
            return f'Could not access TMRemote folder: {ex}'

        if not self.prevBanDetection:
            self.prevBanDetection = status

        return gm_status

    def run(self):
        print(f'inside BanDetect: {self.sleep_time}')
        while True:
            self.parseBanDetection()
            print(f'got BanDetect: {self.sleep_time}')

            time.sleep(self.sleep_time)
