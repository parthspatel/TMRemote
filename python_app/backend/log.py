import time

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class LogThread(QThread):
    signal = pyqtSignal(str, str)

    def __init__(self):
        QThread.__init__(self)
        self.msg = ''

    def __del__(self):
        self.wait()

    def post(self, msg):
        self.msg = msg

    def getSignal(self):
        return self.signal

    def run(self):
        time.sleep(5)
        self.signal.emit(self.msg)
