import os

import requests
from PyQt5.QtCore import QThread

from backend.auth import Auth
from backend.log import Log

class MaintenanceCheckThread(QThread):
    def __init__(self, username, password, api_key, tm_path, maintenanceWidget, logs, links):
        QThread.__init__(self)
        self.get_username = username
        self.get_password = password
        self.api_key = api_key

        self.tm_path = tm_path

        self.maintenanceWidget = maintenanceWidget
        self.crashCheckBox = self.maintenanceWidget.crashCheckBox
        self.restartCheckBox = self.maintenanceWidget.restartCheckBox
        self.startBotsCheckBox = self.maintenanceWidget.startBotsCheckBox

        self.links = links
        self.logs = logs

        self.notified = False
        self.maintenance = False

        self.sleep_time = 60
        self.sleep_time_const = self.sleep_time

    def __del__(self):
        self.wait()

    @Auth.authenticate(level='basic')
    def __getMaintenanceStatus(self):
        data = {'key': self.api_key(),
                'name': self.get_username()}
        maintenanceStatus = requests.post(
            self.links['MaintenanceCheck'], data=data).text
        return bool(maintenanceStatus)

    @Log.log
    def __maintenanceCheck(self):
        if not self.__getMaintenanceStatus():
            if not self.startBotsCheckBox.isChecked():
                return
            if not self.maintenance:
                return
            self.maintenance = False
            return
        self.maintenance = True
        if self.restartCheckBox.isChecked():
            os.system('shutdown -r -f -t 0')
        elif self.crashCheckBox.isChecked():
            os.system('Taskkill -IM TerminalManager.exe -F')
            os.system('Taskkill -IM Maplestory.exe -F')
            return 'Terminated Manager and Maplestory instances'
        else:
            if self.notified:
                return
            self.notified = True
            return 'Maplestory is now on maintenance'

    def run(self):
        while True:
            self.__maintenanceCheck()
            self.sleep(self.sleep_time)
