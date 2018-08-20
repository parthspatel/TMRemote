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

from backend.profileParser import ProfileManager as ProfileFixer # Because this file is called profileManager

class profileThread(QThread):

    def __init__(self, username, password, apikey, profilesDir, tmPath, logs):
        QThread.__init__(self)

        self.getUsername = username
        self.getPassword = password
        self.getApiKey = apikey

        self.getProfilesDir = profilesDir
        self.getTmPath = tmPath

        self.logs = logs

        self.sleep_time = 10

    def __del__(self):
        self.wait()

    #@Auth.authenticate(level='basic')
    def __getProfiles(self):
        rootdir = self.getProfilesDir()
        for folder, subs, files in os.walk(rootdir):
        	for filename in files:
        		filepath = os.path.join(folder, filename)
        		if filepath.endswith('.xml'):
        			yield filepath

    @Log.log
    def __modifyProfiles(self):
        script_path = self.getTmPath().replace('TerminalManager.exe','TMRemote/Scripts/Logger.py')
        if os.path.isfile(script_path):
            for file in self.__getProfiles():
                if ProfileFixer().enableScript(profilePath=file,
                                               script_path=script_path):
                    return 'Enabled script in XML files'


    def run(self):
        while True:
            # Enable script
            self.__modifyProfiles()
            # Sleep
            self.sleep(self.sleep_time)
