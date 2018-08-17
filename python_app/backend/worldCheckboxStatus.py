import datetime
import os
import pickle

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class worldCheckBoxThread(QThread):
    def __init__(self, banDetectionWidget, tmPath):
        QThread.__init__(self)
        self.worldCheckBoxes = banDetectionWidget.worldCheckBoxes
        self.tmPath = tmPath
        self.sleep_time = 1

    def __getStatus(self):
        status = {}
        for world in self.worldCheckBoxes:
            status[world] = self.worldCheckBoxes[world].isChecked()
        return status

    def __getToCheckPath(self):
        return self.tmPath().replace('TerminalManager.exe','TMRemote/temp/WorldToCheck')

    def __writeStatus(self):
        try:
            os.remove(self.__getToCheckPath())
        except FileNotFoundError:
            pass
        except PermissionError:
            pass
        with open(self.__getToCheckPath(),'wb') as toCheckFile:
            pickle.dump(self.__getStatus(), toCheckFile)

    def run(self):

        while True:
            self.__writeStatus()
            self.sleep(self.sleep_time)
