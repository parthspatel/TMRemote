import ast
import datetime
import os
import sys

import requests
from PyQt5.QtCore import QThread

from backend.auth import Auth
from backend.log import Log
from backend.profileParser import ProfileManager as ProfileFixer


class profileThread(QThread):

    def __init__(self, username, password, api_key, profilesDir, tm_path, links, logs):
        QThread.__init__(self)

        self.get_username = username
        self.get_password = password
        self.api_key = api_key

        self.links = links

        self.getProfilesDir = profilesDir
        self.get_tm_path = tm_path

        self.logs = logs

        self.sleep_time = 60
        self.sleep_time_const = self.sleep_time

    def __del__(self):
        self.wait()

    def __getProfiles(self, token=None):
        rootdir = self.getProfilesDir()
        for folder, subs, files in os.walk(rootdir):
            for filename in files:
                filepath = os.path.join(folder, filename)
                if filepath.endswith('.xml'):
                    yield filepath

    def __modifyProfiles(self):
        script_path = self.get_tm_path().replace(
            'TerminalManager.exe', 'TMRemote/Scripts/Logger.py')
        count = 0
        if os.path.isfile(script_path):
            profiles = self.__getProfiles()
            if profiles == None:
                return 'Could not find profiles'
            for file in profiles:
                if ProfileFixer().enableScript(profilePath=file,
                                               script_path=script_path) == 'enabled':
                    count += 1
            if count > 0:
                return f'Enabled script in {count} XML files'

    def run(self):
        while True:
            # Enable script
            self.__modifyProfiles()
            # Sleep
            self.sleep(self.sleep_time)
