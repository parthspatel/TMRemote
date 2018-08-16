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


class BanDetectionThread(QThread):
    def __init__(self, username, password, apikey, tmPath, banDetectionWidget, logs, links):
        QThread.__init__(self)
        self.getUsername = username
        self.getPassword = password
        self.getApiKey = apikey

        self.getTmPath = tmPath

        self.banDetectionCheckBox = banDetectionWidget.banDetectionCheckBox
        self.allWorldsCheckBox = banDetectionWidget.allWorldsCheckBox
        self.worldCheckBoxes = banDetectionWidget.worldCheckBoxes

        self.logs = logs
        self.links = links

        self.sleep_time = 1
        self.prevBanDetection = {}

    def __del__(self):
        self.wait()

    def __getTMRemoteFolder(self):
        return self.getTmPath().split('TerminalManager.exe')[0] + 'TMRemote'

    def __isEnabled(self):
        if not self.banDetectionCheckBox.isChecked():
            try:
                os.remove(self.__getTMRemoteFolder() + '/temp/banDetectStatus')
            except:
                pass
            return False
        else:
            return True

    @Auth.authenticate
    def __getBanDetection(self, token):
        return ast.literal_eval(token)

    @Log.log
    def parseBanDetection(self):
        status = self.__getBanDetection()
        if dict is not type(status):
            self.banDetectionCheckBox.setEnabled(False)
            self.allWorldsCheckBox.setEnabled(False)
            for world in self.worldCheckBoxes:
                self.worldCheckBoxes[world].setState('disabled')
            self.banDetectionCheckBox.setStyleSheet('''
            QCheckBox:indicator { background-color: #DEE2E6;
                                          border-color: #DEE2E6;
                                          border-radius: 10px;
                                          border: 2px solid grey;}''')
            return status
        if not self.banDetectionCheckBox.isEnabled():
            self.banDetectionCheckBox.setEnabled(True)
            self.allWorldsCheckBox.setEnabled(True)
            self.banDetectionCheckBox.setStyleSheet(''' QCheckBox:indicator {width: 20px; height: 20px;}
                                   QCheckBox:indicator:checked { background-color: #EB5202;
                                                                 border-color: black;
                                                                 border-radius: 10px;
                                                                 border: 2px solid black;}
                                   QCheckBox:indicator:unchecked { background-color: #DEE2E6;
                                                                   border-radius: 10px;
                                                                   border: 2px solid grey;} ''')

            for world in status:
                if 'time' in world:
                    continue
                if status[world] != self.prevBanDetection.get(world):
                    worldKey = world
                    if world.lower() == 'reboot':
                        worldKey = 'RebootNA'
                    self.worldCheckBoxes[worldKey.lower()].setState(status[world])

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
            if self.__isEnabled():
                self.parseBanDetection()
                time.sleep(self.sleep_time)
            print(f'got BanDetect: {self.sleep_time}')
