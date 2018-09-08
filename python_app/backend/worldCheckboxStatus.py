import datetime
import os
import pickle

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class WorldCheckBoxThread(QThread):
    def __init__(self, banDetectionWidget, tmPath):
        QThread.__init__(self)
        self.worldCheckBoxes = banDetectionWidget.worldCheckBoxes
        self.tmPath = tmPath
        self.sleep_time = 10

    def __getStatus(self):
        status = {}
        for world in self.worldCheckBoxes:
            status[world] = self.worldCheckBoxes[world].isChecked()
        return status

    def __getToCheckPath(self):
        return self.tmPath().replace('TerminalManager.exe', 'TMRemote/temp/WorldToCheck')

    def __writeStatus(self):
        try:
            os.remove(self.__getToCheckPath())
        except FileNotFoundError:
            pass
        except PermissionError:
            pass
        tmPath = self.tmPath().split('TerminalManager.exe')[0]
        if self.tmPath() is None:
            return
        scriptsFolder = tmPath + 'TMRemote/Scripts'
        tmRemoteFolder = tmPath + 'TMRemote'
        if not os.path.isdir(tmRemoteFolder):
            os.mkdir(tmRemoteFolder)
        if not os.path.isdir(scriptsFolder):
            os.mkdir(scriptsFolder)
        if not os.path.isdir(tmRemoteFolder + '/temp'):
            os.mkdir(tmRemoteFolder + '/temp')
        with open(self.__getToCheckPath(), 'wb') as toCheckFile:
            pickle.dump(self.__getStatus(), toCheckFile)

    def run(self):

        while True:
            self.__writeStatus()
            self.sleep(self.sleep_time)
