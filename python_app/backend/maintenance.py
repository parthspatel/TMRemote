from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from backend.auth import Auth
from backend.log import Log

import requests
import os

class MaintenanceCheckThread(QThread):
    def __init__(self, username, password, apikey, maintenanceWidget, logs, links):
        QThread.__init__(self)
        self.getUsername = username
        self.getPassword = password
        self.getApiKey = apikey

        self.maintenanceWidget = maintenanceWidget
        self.crashCheckBox = self.maintenanceWidget.crashCheckBox
        self.restartCheckBox = self.maintenanceWidget.restartCheckBox

        self.links = links
        self.logs = logs

        self.notified = False

        self.sleep_time= 5

    def __del__(self):
        self.wait()

    @Auth.authenticate(level='basic')
    def __getMaintenanceStatus(self):
        data = {'key': self.getApiKey(),
                'name': self.getUsername()}
        maintenanceStatus = requests.post(self.links['MaintenanceCheck'], data=data).text
        return bool(maintenanceStatus)

    @Log.log
    def __maintenanceCheck(self):
        if self.__getMaintenanceStatus():
            if self.restartCheckBox.isChecked():
                #os.system('shutdown -r -f -t 0')
                return 'Restarting pc' #remove in live version
            elif self.crashCheckBox.isChecked():
                # os.system('Taskkill -IM TerminalManager.exe -F')
                # os.system('Taskkill -IM Maplestory.exe -F')
                return 'killing maple' #remove in live version
            else:
                if not self.notified:
                    return 'Maplestory is now on maintenance'
                    self.notified = True



    def run(self):
        while True:
            self.__maintenanceCheck()
            self.sleep(self.sleep_time)
