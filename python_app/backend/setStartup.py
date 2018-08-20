from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from backend.auth import Auth
from backend.log import Log

import requests
import os
import sys

from winreg import *

class setStartupThread(QThread):
    def __init__(self, username, password, apikey, tmPath, logs, links):
        QThread.__init__(self)
        self.getUsername = username
        self.getPassword = password
        self.getApiKey = apikey

        self.tmPath = tmPath

        self.logs = logs
        self.links = links

        self.sleep_time = 30

    def __del__(self):
        self.wait()

    def __getCurrentPath(self):
        if getattr(sys, 'frozen', False):
            # compiled
            dir_ = os.path.dirname(sys.executable)
        else:
            # uncompiled
            dir_ = os.path.dirname(os.path.realpath(__file__))
        return dir_

    @Log.log
    def __WriteRegistry(self):
        TMRExePath = self.__getCurrentPath() + '\TMRemote.exe'
        aReg = ConnectRegistry(None,HKEY_LOCAL_MACHINE)

        aKey = OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run", 0, KEY_ALL_ACCESS)
        try:
            SetValueEx(aKey,"TMRemote",0, REG_SZ, TMRExePath)
            return f'Added TMRemote to startup programs'
        except EnvironmentError:
            return f'Failed to add TMRemote to startup programs'

        CloseKey(aKey)
        CloseKey(aReg)

    def run(self):
        while True:
            self.__WriteRegistry()
            self.sleep(self.sleep_time)
