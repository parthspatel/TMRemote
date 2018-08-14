import ast
import pprint as pp
import time
import requests
import ast
import pickle
import os
import urllib.request
import datetime

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def getCurrentPath():
    if getattr(sys, 'frozen', False):
        dir = os.path.dirname(sys.executable)
    else:
        dir = os.path.dirname(os.path.realpath(__file__))
    return dir

class MainThread(QThread):

    def __init__(self, username, password, apikey, profilesDir, tmPath, logs, banDetect, MaintenanceWidget):
        QThread.__init__(self)

        self.getUsername = username
        self.getPassword = password
        self.getApiKey = apikey

        self.getProfilesDir = profilesDir
        self.getTmPath = tmPath
        self.filePaths = {'TerminalManagerFolder':self.getTmPath()}
        self.TMRemoteFolder = '' # Sorry parth, but can't make dict recursive

        self.baseData = {}

        self.version = 0.1

        self.logs = logs

        self.previousBanState = {}
        self.banDetect = banDetect

        self.maintenance = MaintenanceWidget

        self.links = {'botLogs': 'https://tmremote.io/api/v1/activity',
                      'banDetection': 'https://tmremote.io/api/v1/gm/status',
                      'banPost': '',
                      'tmLog': '',
                      'ExeDownload':'',
                      'VersionCheck':'',
                      'MaintenanceCheck':''}

    def __del__(self):
        self.wait()

<<<<<<< HEAD
    def authenticate(func):
        def authenticate_and_call(*args, **kwargs):
            token = args[0].__auth()
            if 'error' in token:
                print('Authentication Failed')
                args[0].sleep_time = 10
                return
            return func(token=token,
                        *args, **kwargs)
        return authenticate_and_call

    def __auth(self):
        data = {'key': self.getApiKey() + 'ad',
                'name': self.getUsername()}
        return requests.post(self.links['banDetection'],
                             data=data).text

    @authenticate
    def getBanDetection(self, token):
        return ast.literal_eval(token)
=======
    def __FolderCheck(self, path):
        if not os.path.exists(path):
            os.makedirs(path)

    def __UpdateTMRLogs(self, text, timestamp=True):
        now = datetime.datetime.now().isoformat(' ','seconds')
        if timestamp:
            msg = '[{}]: {}'.format(now, text)
        else: msg = text
        self.logs.append(msg)

    def __UpdateExe(self):
        newVersion = requests.post(self.links['VersionCheck'], data = self.baseData).text
        if int(newVersion) > self.version:
            currentPath = getCurrentPath()
            newNamePath = currentPath.split('TMRemote.exe')[0] + '/TMRemote_old.exe'
            os.rename(currentPath, newNamePath)
            urllib.request.urlretrieve(self.links['ExeDownload'], currentPath)
            os.remove(newNamePath)
        else: return

    def __UpdateVariables(self):
        self.baseData = {'key': self.getApiKey(),
                         'name':self.getUsername()}
        self.filePaths['TerminalManagerFolder'] = self.getTmPath().split('TerminalManager.exe')[0]
        self.TMRemoteFolder = self.filePaths['TerminalManagerFolder'] + '/TMRemote'

    def authenticate(self):
        return requests.post(self.links['botLogs'], data=self.baseData).text

    def __WatchTheseWorlds(self):
        pickleData = {}
        for world in self.banDetect.worldCheckBoxes:
            pickleData[world] = self.banDetect.worldCheckBoxes[world].isChecked()
        try:
            os.remove(self.TMRemoteFolder + '/WorldToCheck')
        except FileNotFoundError: pass

        with open(self.TMRemoteFolder + '/WorldToCheck', 'wb') as pickleFile:
            pickle.dump(pickleData, pickleFile)

    def __ServerStatus(self):
        return bool(requests.post(self.links['MaintenanceCheck'], data = self.baseData).text)

    def __MaintenanceCheck(self):
        serverStatus = self.__ServerStatus()
        if self.maintenance.crashCheckBox.isChecked() and serverStatus:
            os.system('shutdown -r -f -t 0')
        if self.maintenance.restartCheckBox.isChecked() and serverStatus:
            os.system('Taskkill /IM TerminalManager.exe /F')
            os.system('Taskkill /IM Maplestory.exe /F')
            self.__UpdateTMRLogs('Maplestory is now on maintenance.')

    def __GetBanLogs(self):
        if self.banDetect.banDetectionCheckBox.isChecked():
            response = requests.post(self.links['banDetection'], data=self.baseData).text
            if 'error' in response:
                self.banDetect.banDetectionCheckBox.setEnabled(False)
                self.banDetect.banDetectionCheckBox.setToolTip('No access to Ban Detection, please upgrade your license to gain access')
                self.__UpdateTMRLogs('No access to Ban Detection, please upgrade your license to gain access')
                self.banDetect.banDetectionCheckBox.setChecked(False)
            dictionaryResponse = ast.literal_eval(response.lower())
            pickleData = {}
            GMStringUpdate = ''
            for world in self.banDetect.worldCheckBoxes:
                worldValue = dictionaryResponse[world]
                pickleData[world] = worldValue
                if worldValue != self.previousBanState.get(world):
                    self.banDetect.worldCheckBoxes[world].setState(worldValue)
                    now = datetime.datetime.now().isoformat(' ','seconds')
                    GMStringUpdate += '[{}]: GM is now {} in {}\n'.format(now, worldValue, world)
                    self.previousBanState[world] = worldValue
            if GMStringUpdate != '':
                self.__UpdateTMRLogs(GMStringUpdate, timestamp = False)
            try:
                os.remove(self.TMRemoteFolder + '/GMStatus')
            except FileNotFoundError: pass

            with open(self.TMRemoteFolder + '/GMStatus', 'wb') as pickleFile:
                pickle.dump(pickleData, pickleFile)
        else: return
>>>>>>> 490f72c7e6222ba58af2ff43a461ca492f093ac8

    def run(self):
        self.sleep_time = 1
        while(True):
<<<<<<< HEAD
            status = self.getBanDetection()
            pp.pprint(status)
            time.sleep(self.sleep_time)
=======
            # Update the username and password from QtSettings window,
            # has to be called before any other http request. (aka in begin of loop)
            self.__UpdateVariables()

            response = self.authenticate()
            if not response == 'success': continue # Next iteration.

            self.__FolderCheck(path=self.TMRemoteFolder)


            try:

                # Check if update is available
                self.__UpdateExe()

                # Check if maintenance checkboxes are ticked, if they are, check what to do
                self.__MaintenanceCheck()

            except requests.exceptions.MissingSchema: # We have no link yet
                pass

            # Get other users their ban logs if available to the user
            self.__GetBanLogs()

            # Define which worlds to check in the clients
            self.__WatchTheseWorlds()
>>>>>>> 490f72c7e6222ba58af2ff43a461ca492f093ac8
