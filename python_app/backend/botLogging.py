import ast
import datetime
import os
import pickle
import time

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from backend.auth import Auth
from backend.log import Log


class BotLogging(QThread):
    def __init__(self, username, password, apikey, tmPath, worldCheckBoxes, logs, links):
        QThread.__init__(self)
        self.getUsername = username
        self.getPassword = password
        self.getApiKey = apikey

        self.getTmPath = tmPath

        self.worldCheckBoxes = worldCheckBoxes

        self.logs = logs
        self.links = links

        self.sleep_time = 10
        self.prevBanDetection = {}
