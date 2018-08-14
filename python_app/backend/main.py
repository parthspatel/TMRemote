import ast
import datetime
import os
import pickle
import pprint as pp
import time
import urllib.request

import requests
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from backend.log import LogThread


def getCurrentPath():
    if getattr(sys, 'frozen', False):
        dir = os.path.dirname(sys.executable)
    else:
        dir = os.path.dirname(os.path.realpath(__file__))
    return dir


class MainThread(QThread):

    def __init__(self, username, password, apikey, profilesDir, tmPath, logs):
        QThread.__init__(self)

        self.getUsername = username
        self.getPassword = password
        self.getApiKey = apikey

        self.getProfilesDir = profilesDir
        self.getTmPath = tmPath
        self.filePaths = {'TerminalManagerFolder': self.getTmPath()}
        self.TMRemoteFolder = ''  # Sorry parth, but can't make dict recursive

        self.logs = logs

        self.links = {'botLogs': 'https://tmremote.io/api/v1/activity',
                      'banDetection': 'https://tmremote.io/api/v1/gm/status',
                      'banPost': '',
                      'tmLog': '',
                      'ExeDownload': '',
                      'VersionCheck': '',
                      'MaintenanceCheck': ''}

    def __del__(self):
        self.wait()

    def authenticate(func):
        def authenticate_and_call(*args, **kwargs):
            token = args[0].__auth()
            if 'error' in token:
                print('Authentication Failed')
                args[0].sleep_time = 10
                return None

            return func(token=token,
                        *args, **kwargs)
        return authenticate_and_call

    def __auth(self):
        data = {'key': self.getApiKey(),
                'name': self.getUsername()}
        return requests.post(self.links['banDetection'],
                             data=data).text

    def log(func):
        def log_output(*args, **kwargs):
            now = datetime.datetime.now().isoformat(' ', 'seconds')
            message = '{}: {}'.format(now, func(*args, **kwargs))

            args[0].logs.post(message)
        return log_output

    @authenticate
    def getBanDetection(self, token):
        return ast.literal_eval(token)

    @log
    def parseBanDetection(self):
        status = self.getBanDetection()
        if not status:
            return 'Upgrade to unlock Ban Detection'

    def run(self):
        self.sleep_time = 0
        while(True):

            status = self.parseBanDetection()

            # pp.pprint(status)
            time.sleep(self.sleep_time)
