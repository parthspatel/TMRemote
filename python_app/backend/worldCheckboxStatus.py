import datetime
import os
import pickle

from PyQt5.QtCore import QThread

class WorldCheckBoxThread(QThread):
    def __init__(self, banDetectionWidget, tm_path):
        QThread.__init__(self)
        self.worldCheckBoxes = banDetectionWidget.worldCheckBoxes
        self.tm_path = tm_path
        self.sleep_time = 10

    def __getStatus(self):
        status = {}
        for world in self.worldCheckBoxes:
            status[world] = self.worldCheckBoxes[world].isChecked()
        return status

    def __getToCheckPath(self):
        return self.tm_path().replace('TerminalManager.exe', 'TMRemote/temp/WorldToCheck')

    def __write_status(self):
        try:
            os.remove(self.__getToCheckPath())
        except FileNotFoundError:
            pass
        except PermissionError:
            pass
        tm_path = self.tm_path().split('TerminalManager.exe')[0]
        if self.tm_path() is None:
            return
        scriptsFolder = tm_path + 'TMRemote/Scripts'
        tmRemoteFolder = tm_path + 'TMRemote'
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
            if not self.tm_path() in [None, 'None']:
                self.__write_status()
            self.sleep(self.sleep_time)
