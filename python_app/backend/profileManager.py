import ast
import datetime
import os
import sys

import requests
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from backend.auth import Auth
from backend.log import Log
from backend.profileParser import ProfileManager as ProfileFixer


class profileThread(QThread):

    def __init__(self, username, password, apikey, profilesDir, tmPath, links, logs):
        QThread.__init__(self)

        self.getUsername = username
        self.getPassword = password
        self.apiKey = apikey

        self.links = links

        self.getProfilesDir = profilesDir
        self.getTmPath = tmPath

        self.logs = logs

        self.sleep_time = 60
        self.sleep_time_const = self.sleep_time

    def __del__(self):
        self.wait()

    @Auth.authenticate(level='basic')
    def __getProfiles(self, token):
        rootdir = self.getProfilesDir()
        for folder, subs, files in os.walk(rootdir):
            for filename in files:
                filepath = os.path.join(folder, filename)
                if filepath.endswith('.xml'):
                    print(filepath)
                    yield filepath

    @Log.log
    def __modifyProfiles(self):
        script_path = self.getTmPath().replace(
            'TerminalManager.exe', 'TMRemote/Scripts/Logger.py')
        count = 0
        if os.path.isfile(script_path):
            profiles = self.__getProfiles()
            if profiles == None:
                return 'Could not find profiles'
            for file in profiles:
                if ProfileFixer().enableScript(profilePath=file,
                                               script_path=script_path):
                    count += 1
            if count > 0:
                return f'Enabled script in {count} XML files'

    def run(self):
        while True:
            # Enable script
            self.__modifyProfiles()
            # Sleep
            self.sleep(self.sleep_time)
