import ast
import os
import pickle

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
        self.apiKey = apikey

        self.getTmPath = tmPath

        self.banDetectionCheckBox = banDetectionWidget.banDetectionCheckBox
        self.allWorldsCheckBox = banDetectionWidget.allWorldsCheckBox
        self.worldCheckBoxes = banDetectionWidget.worldCheckBoxes

        self.logs = logs
        self.links = links

        self.sleep_time = 30
        self.sleep_time_const = self.sleep_time
        self.prevBanDetection = {}

        self.noAccessMessage = 'Please upgrade your license to gain access to ban detection'
        self.checkBoxGreyscale = '''
        QCheckBox:indicator { background-color: #DEE2E6;
                                      border-color: #DEE2E6;
                                      border-radius: 10px;
                                      border: 2px solid grey;}'''

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

    @Auth.authenticate(level='prime')
    def __getBanDetection(self, token):
        return token

    @Log.log
    def parseBanDetection(self):
        gmStatus = self.__getBanDetection()
        if not gmStatus:
            return f'Ban Status Failed Auth: {gmStatus}'
        if 'error' in gmStatus.lower() or 'fail' in gmStatus.lower():
            return gmStatus

        print(gmStatus)
        GMLogs = ast.literal_eval(gmStatus)
        if gmStatus.status_code == 401:
            self.banDetectionCheckBox.setEnabled(False)
            self.banDetectionCheckBox.setToolTip(self.noAccessMessage)
            self.allWorldsCheckBox.setEnabled(False)
            self.allWorldsCheckBox.setToolTip(self.noAccessMessage)
            for world in self.worldCheckBoxes:
                self.worldCheckBoxes[world].setEnabled(False)
                self.worldCheckBoxes[world].setToolTip(self.noAccessMessage)
                self.worldCheckBoxes[world].setState('disabled')
                self.worldCheckBoxes[world].setStyleSheet(
                    self.checkBoxGreyscale)
            self.banDetectionCheckBox.setStyleSheet(self.checkBoxGreyscale)
            return GMLogs
        if not self.banDetectionCheckBox.isEnabled():
            self.banDetectionCheckBox.setEnabled(True)
            self.allWorldsCheckBox.setEnabled(True)
            self.banDetectionCheckBox.setStyleSheet('''
                                   QCheckBox:indicator {width: 20px; height: 20px;}
                                   QCheckBox:indicator:checked { background-color: #EB5202;
                                                                 border-color: black;
                                                                 border-radius: 10px;
                                                                 border: 2px solid black;}
                                   QCheckBox:indicator:unchecked { background-color: #DEE2E6;
                                                                   border-radius: 10px;
                                                                   border: 2px solid grey;} ''')

            for world in GMLogs:
                if GMLogs[world]['status'] != self.prevBanDetection.get(world):
                    self.worldCheckBoxes[world.lower()].setState(
                        GMLogs[world])

        gm_status = []
        for world in GMLogs:
            if GMLogs[world]['status'] != self.prevBanDetection.get(world):
                self.worldCheckBoxes[world.lower()].setState(
                    GMLogs[world]['status'])

                gm_status.append('BD Status: {} in {}'.format(
                    GMLogs[world]['status'], GMLogs[world]['name']))
                self.prevBanDetection[world] = GMLogs[world]['status']

        try:
            if self.__getTMRemoteFolder():
                if not os.path.exists(self.__getTMRemoteFolder() + '/temp'):
                    os.makedirs(self.__getTMRemoteFolder() + '/temp')
                with open(self.__getTMRemoteFolder() + '/temp/banDetectStatus', 'wb+') as file:
                    pickle.dump(str(GMLogs), file)
            else:
                return
        except Exception as ex:
            return f'Could not access TMRemote folder: {ex}'

        if not self.prevBanDetection:
            self.prevBanDetection = GMLogs

        return gm_status

    def run(self):
        while True:
            if self.__isEnabled():
                self.parseBanDetection()

            self.sleep(self.sleep_time)
