import ast
import datetime
import difflib
import os

import requests
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from backend.auth import Auth
from backend.log import Log


class TMLoggingThread(QThread):
    def __init__(self, username, password, apikey, tmPath, logs, links):
        QThread.__init__(self)
        self.getUsername = username
        self.getPassword = password
        self.apiKey = apikey

        self.getTmPath = tmPath

        self.logs = logs
        self.links = links

        self.sleep_time = 60
        self.sleep_time_const = self.sleep_time

        self.prevLog = None

    def __del__(self):
        self.wait()

    def __getFilePath(self):
        return self.getTmPath().split('TerminalManager.exe')[0] + '/TerminalManager.log'

    def __createPreviousContentFile(self, oldContent):
        with open(self.__getFilePath().replace('TerminalManager.log', '/TMRemote/TerminalManager.previous.log'), 'w') as LogFile:
            LogFile.write(oldContent)

    def __getPreviousLogs(self):
        try:
            with open(self.__getFilePath().replace('TerminalManager.log', '/TMRemote/TerminalManager.previous.log'), 'r') as LogFile:
                return LogFile.read()
        except Excption as ex:
            raise ex

    def __getDifference(self, oldLogs, newLogs):
        matcher = difflib.SequenceMatcher(None, oldLogs, newLogs)

        def process_tag(tag, i1, i2, j1, j2):
            if tag == 'replace':
                return matcher.newLogs[j1:j2]
            if tag == 'delete':
                return matcher.oldLogs[i1:i2]
            if tag == 'equal':
                return ''
            if tag == 'insert':
                return matcher.newLogs[j1:j2]
            assert false, "Unknown tag %r" % tag
        return ''.join(process_tag(*t) for t in matcher.get_opcodes())

    def __getFileContent(self):
        try:
            with open(self.__getFilePath(), 'r') as managerLogFile:
                fullLogs = managerLogFile.read()
                self.__createPreviousContentFile(fullLogs)
                logDifference = self.__getDifference(self.__getPreviousLogs(), fullLogs)
                return logDifference
        except Exception as ex:
            raise ex

    @Auth.authenticate(level='tManagerLogs')
    @Log.log
    def __postManagerLogs(self, token):
        try:
            status = self.__getFileContent()
        except Exception as ex:
            return f'Error getting Terminal Manager Logs: {ex}'

        try:
            requests.post(self.links['tmLog'], data=status)
        except Exception as ex:
            return f'No Internet: {ex}'

    def run(self):

        while True:
            self.__postManagerLogs()
            self.sleep(self.sleep_time)
