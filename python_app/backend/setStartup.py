import os
import subprocess
import sys
from winreg import *

import psutil
import requests
from PyQt5.QtCore import QThread

from backend.auth import Auth
from backend.log import Log


class setStartupThread(QThread):
    def __init__(self, username, password, api_key, tm_path, logs, links, generalSettings):
        QThread.__init__(self)
        self.get_username = username
        self.get_password = password
        self.api_key = api_key

        self.tm_path = tm_path

        self.generalSettings = generalSettings

        self.logs = logs
        self.links = links

        self.setStartup = True

        self.processName = 'terminalmanager.exe'

        self.sleep_time = 60
        self.sleep_time_const = self.sleep_time

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
            aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
            aKey = OpenKey(
                aReg, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, KEY_ALL_ACCESS)
            try:
                SetValueEx(aKey, "TMRemote", 0, REG_SZ, TMRExePath)
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
    def __startTerminalManager(self, token=None):
        if not self.generalSettings.startManagerCheckBox.isChecked():
            return
        if self.__terminalIsActive():
            return
        subprocess.call(self.tm_path(), cwd=self.tm_path().split('TerminalManager.exe')[0], shell = True)
        return 'Started Terminal Manager'

    def run(self):
        while True:
            self.__startTerminalManager()
            self.sleep(self.sleep_time)
