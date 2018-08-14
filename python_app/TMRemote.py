import ctypes
import os
import sys
from multiprocessing import Queue

from gui import *


def main():
    if not isUserAdmin():
        print("> User account does not have admin controls, rerunning with admin controls")
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, getCurrentPath(), None, 1)

    app = runApp(TMRemoteApp)
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


def runApp(application):
    app = QApplication(sys.argv)
    ui = application()
    ui.show()
    return app.exec_()


def closeApp(app):
    sys.exit(app)


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
