import datetime
import time

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class LogThread(QThread):
    signal_str = pyqtSignal(str, str)
    signal_list = pyqtSignal(str, list)

    def __init__(self):
        QThread.__init__(self)
        self.msg = ''

    def __del__(self):
        self.wait()

    def post(self, time, msg):
        self.time = time
        self.msg = msg

    def getSignal(self):
        if list is type(self.msg):
            return self.signal_list
        return self.signal_str

    def run(self):
        time.sleep(5)
        if list is type(self.msg):
            self.signal_list.emit(self.time, self.msg)
        else:
            self.signal_str.emit(self.time, self.msg)


class Log():
    def log(func):
        def log_output(*args, **kwargs):
            now = datetime.datetime.now().isoformat(' ', 'seconds')
            message = func(*args, **kwargs)
            if message:
                args[0].logs.post(now, message)
                return f'{now}: {message}'
        return log_output
