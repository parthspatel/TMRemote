from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from backend.auth import Auth
from backend.log import Log

import requests
import os
import sys

from winreg import *

import psutil

class setStartupThread(QThread):
    def __init__(self, username, password, apikey, tmPath, logs, links):
        QThread.__init__(self)
        self.getUsername = username
        self.getPassword = password
        self.getApiKey = apikey

        self.tmPath = tmPath

        self.logs = logs
        self.links = links

        self.setStartup = False

        self.processName = 'terminalmanager.exe'

        self.sleep_time = 30

    def __del__(self):
        self.wait()

    def __getCurrentPath(self):
        if getattr(sys, 'frozen', False):
            # compiled
            dir_ = os.path.dirname(sys.executable + '\TMRemote.exe')
        else:
            # uncompiled
            dir_ = os.path.dirname(os.path.realpath(__file__))
        return dir_

    @Log.log
    def __WriteRegistry(self):
        if not self.setStartup:
            TMRExePath = self.__getCurrentPath()
            aReg = ConnectRegistry(None,HKEY_CURRENT_USER)
            aKey = OpenKey(aReg, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, KEY_ALL_ACCESS)
            try:
                SetValueEx(aKey,"TMRemote",0, REG_SZ, TMRExePath)
                self.setStartup = True
                return 'Added TMRemote to startup programs'
            except EnvironmentError:
                self.setStartup = False
                return 'Failed to add TMRemote to startup programs'

            CloseKey(aKey)
            CloseKey(aReg)

    def __terminalIsActive(self):
        for process in psutil.process_iter():
            if process.name().lower() == self.processName:
                return True
            return False

    @Log.log
    @Auth.authenticate(level='basic')
    def __startTerminalManager(self):
        if not self.__terminalIsActive():
            os.startfile(self.tmPath())
            return 'Started Terminal Manager'

    def run(self):
        while True:
            self.__WriteRegistry()
            self.__startTerminalManager()
            self.sleep(self.sleep_time)
