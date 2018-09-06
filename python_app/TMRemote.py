import ctypes
import os
import sys
from multiprocessing import Queue
import requests, re

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from gui import TMRemote


def main():
    if not isUserAdmin():
        print("> User account does not have admin controls, rerunning with admin controls")
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, getCurrentPath(), None, 1)

    app = runApp(TMRemote)
    exeUpdate(ui)
    # anything after runApp will occur AFTER the application is closed
    closeApp(app)


def isUserAdmin():
    '''
    Return True if user has admin privilege
    Raises:
        AdminStateUnknownError if user privileges cannot be determined
    '''
    try:
        return os.getuid() == 0
    except AttributeError:
        pass
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() == 1
    except AttributeError:
        raise AdminStateUnknownError


def exeUpdate(application):
    #                  'ExeDownload': 'https://mehodin.com/TMRemote.exe',
    version = '0.1'
    execVersion = requests.get('https://mehodin.com/execVersion.html').text
    execVersion = re.search('<p>(.*)</p>', execVersion).group(1)
    if version == execVersion:
        return
    application.destroy()
    execContent = requests.get('https://mehodin.com/i/TMRemote.exe').content
    print(getCurrentPath() + '\TMRemote.exe')
    with open(getCurrentPath() + '\TMRemote.exe', 'wb') as file:
        file.seek(0)
        file.truncate()
        file.write(execContent)


def runApp(application):
    global ui
    app = QApplication(sys.argv)
    ui = application()
    ui.show()
    return app.exec_()


def closeApp(app):
    pass


def setAppUserModel(app_id='TMRemote'):
    # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)


def getCurrentPath():
    if getattr(sys, 'frozen', False):  # frozen
        dir = os.path.dirname(sys.executable)
    else:  # unfrozen
        dir = os.path.dirname(os.path.realpath(__file__))
    return dir


if __name__ == '__main__':
    main()
