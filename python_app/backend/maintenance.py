from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from backend.auth import Auth
from backend.log import Log
# from backend.clientLauncher import ClientLauncher

import requests
import os

class MaintenanceCheckThread(QThread):
    def __init__(self, username, password, apikey, tmPath, maintenanceWidget, logs, links):
        QThread.__init__(self)
        self.getUsername = username
        self.getPassword = password
        self.apiKey = apikey

        self.tmPath = tmPath

        self.maintenanceWidget = maintenanceWidget
        self.crashCheckBox = self.maintenanceWidget.crashCheckBox
        self.restartCheckBox = self.maintenanceWidget.restartCheckBox
        self.startBotsCheckBox = self.maintenanceWidget.startBotsCheckBox

        self.links = links
        self.logs = logs

        self.notified = False
        self.maintenance = False

        self.sleep_time= 5
        self.sleep_time_const = self.sleep_time

    def __del__(self):
        self.wait()

    @Auth.authenticate(level='basic')
    def __getMaintenanceStatus(self, token):
        data = {'key': self.apiKey,
                'name': self.getUsername()}
        maintenanceStatus = requests.post(self.links['MaintenanceCheck'], data=data).text
        return bool(maintenanceStatus)

    @Log.log
    def __maintenanceCheck(self):
        if self.__getMaintenanceStatus():
            self.maintenance = True
            if self.restartCheckBox.isChecked():
                # os.system('shutdown -r -f -t 0') uncommen in live version
                return 'Restarting pc' #remove in live version
            elif self.crashCheckBox.isChecked():
                # os.system('Taskkill -IM TerminalManager.exe -F') uncomment in live
                # os.system('Taskkill -IM Maplestory.exe -F')
                return 'Killing maple' #remove in live version
                return 'Terminated Manager and Maplestory instances'
            else:
                if not self.notified:
                    return 'Maplestory is now on maintenance'
                    self.notified = True
        else:
            if self.startBotsCheckBox.isChecked():
                if self.maintenance:
                    # clientLauncher().launchClients()
                    self.maintenance = False

    def run(self):
        while True:
            self.__maintenanceCheck()
            self.sleep(self.sleep_time)
