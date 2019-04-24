import ctypes
import os
import sys
from pathlib import Path

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from resources.magicNumbers import MagicNumbers as Magic


class Settings(QMainWindow):
    def __init__(self, parent=None):

        # Initialize QMainWindow as a child of parent
        super(Settings, self).__init__(parent)

        # Set Main Window Variables
        self.title = 'TMR: Settings'

        self.left = 100
        self.top = 100
        self.width = 600
        self.height = 600
        
        if parent:
            parent.update()
            self.left = (parent.width - self.width) / 2 + parent.x()
            self.top = (parent.height - self.height) / 2 + \
                parent.y() + Magic.WINDOW_SPACER_TOP
            

        # Initialize UI
        self.__initUI()

    def __initUI(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowIcon(QIcon('icons\icon.ico'))
        self.setFixedSize(self.width, self.height)

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.mainBox = QVBoxLayout()

        self.loginBox = QGroupBox("TMR Login")
        self.filePathBox = QGroupBox("File Path")

        self.hBoxLogin = QHBoxLayout()
        self.loginWidget = _LoginWidget()
        self.hBoxLogin.addWidget(self.loginWidget)
        self.loginBox.setLayout(self.hBoxLogin)

        self.hBoxLogin = QHBoxLayout()
        self.fileDirWidget = _FileDirWidget()
        self.hBoxLogin.addWidget(self.fileDirWidget)
        self.filePathBox.setLayout(self.hBoxLogin)

        self.mainBox.addWidget(self.loginBox)
        self.mainBox.addWidget(self.filePathBox)

        self.centralWidget.setLayout(self.mainBox)

    def get_username(self):
        return self.loginWidget.get_username()

    def get_password(self):
        return self.loginWidget.get_password()

    def getTextEdits(self):
        return {'loginWidget': self.loginWidget.getTextEdits()}

    def getProfileDir(self):
        return self.fileDirWidget.getProfileDir()

    def get_tm_path(self):
        return self.fileDirWidget.get_tm_path()

    def setUsername(self, username):
        self.loginWidget.setUsername(username)
        self.update()

    def setPassword(self, password):
        self.loginWidget.setPassword(password)
        self.update()

    def setProfileDir(self, dir):
        self.fileDirWidget.setProfileDir(dir)
        self.update()

    def settm_path(self, path):
        self.fileDirWidget.settm_path(path)
        self.update()


class _LoginWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.__initUI()

    def __initUI(self):
        # Username
        usernameLabel = QLabel(self)
        usernameLabel.setText('Login ID:')

        self.__username = QLineEdit(self)
        self.__username.setPlaceholderText('Enter ID')
        # self.__username.setText('john')
        self.__username.setFixedHeight(Magic.HEIGHT)

        # Password
        passwordLabel = QLabel(self)
        passwordLabel.setText('Login PWD:')

        self.__password = QLineEdit(self)
        self.__password.setPlaceholderText('Enter PWD')
        self.__password.setEchoMode(QLineEdit.Password)
        self.__password.setFixedHeight(Magic.HEIGHT)

        # # api_key
        # api_keyLabel = QLabel(self)
        # api_keyLabel.setText('API Key:')
        #
        # self.__api_key = QLineEdit(self)
        # self.__api_key.setPlaceholderText('Enter API Key')
        # self.__api_key.setEchoMode(QLineEdit.Password)
        # self.__api_key.setFixedHeight(Magic.HEIGHT)

        grid = QGridLayout()
        grid.setSpacing(Magic.GRID_SPACE)

        grid.addWidget(usernameLabel, 1, 0)
        grid.addWidget(self.__username, 1, 1)

        grid.addWidget(passwordLabel, 2, 0)
        grid.addWidget(self.__password, 2, 1)

        # grid.addWidget(api_keyLabel, 3, 0)
        # grid.addWidget(self.__api_key, 3, 1)

        self.setLayout(grid)

    def get_username(self):
        return self.__username.text()

    def get_password(self):
        return self.__password.text()

    def getTextEdits(self):
        return {'username': self.__username,
                'password': self.__password}

    # def get_api_key(self):
    #     return self.__api_key.text()

    def setUsername(self, username):
        self.__username.setText(username)
        self.update()

    def setPassword(self, password):
        self.__password.setText(password)
        self.update()

    # def set_api_key(self, api_key):
    #     self.__api_key.setText(api_key)
    #     self.update()


class _FileDirWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.__initUI()

    def __initUI(self):
        # Profiles
        profilesLabel = QLabel(self)
        profilesLabel.setText('Profiles:')

        self.profiles = QLineEdit(self)
        self.profiles.setPlaceholderText('Dir Containing Profiles')
        self.profiles.setReadOnly(True)
        self.profiles.setFixedHeight(Magic.HEIGHT)

        profilesButton = QPushButton(self)
        profilesButton.setIcon(QIcon('icons\open.svg'))
        profilesButton.setFixedWidth(Magic.HEIGHT)
        profilesButton.clicked.connect(self.__onPushGetProfilesDir)

        # Terminal Manager
        terminalLabel = QLabel(self)
        terminalLabel.setText('Terminal\nManager:')

        self.TerminalManager = QLineEdit(self)
        self.TerminalManager.setPlaceholderText(
            'Dir Containing TerminalManager.exe')
        self.TerminalManager.setReadOnly(True)
        self.TerminalManager.setFixedHeight(Magic.HEIGHT)

        terminalButton = QPushButton(self)
        terminalButton.setIcon(QIcon('icons\open.svg'))
        terminalButton.setFixedWidth(Magic.HEIGHT)
        terminalButton.clicked.connect(self.__onPushget_tm_path)

        grid = QGridLayout()
        grid.setSpacing(Magic.GRID_SPACE)

        grid.addWidget(profilesLabel, 1, 0)
        grid.addWidget(self.profiles, 1, 1)
        grid.addWidget(profilesButton, 1, 2)

        grid.addWidget(terminalLabel, 2, 0)
        grid.addWidget(self.TerminalManager, 2, 1)
        grid.addWidget(terminalButton, 2, 2)

        self.setLayout(grid)

    def __onPushGetProfilesDir(self):
        path = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.profiles.setText(path)

    def __onPushget_tm_path(self):
        path = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        if Path(path).is_dir():
            if Path(path + '/TerminalManager.exe').is_file():
                self.TerminalManager.setText(path + '/TerminalManager.exe')
            else:
                err = 'TerminalManager.exe not found in {}'.format(path)
                
        else:
            err = 'Path selected is not a Directory: {}'.format(path)
            

    def getProfileDir(self):
        return self.profiles.text()

    def get_tm_path(self):
        return self.TerminalManager.text()

    def setProfileDir(self, dir):
        self.profiles.setText(str(dir))
        self.update()

    def settm_path(self, path):
        self.TerminalManager.setText(str(path))
        self.update()


class _AdminStateUnknownError(Exception):
    """Cannot determine whether the user is an admin."""
    pass


def isUserAdmin():
    # type: () -> bool
    """Return True if user has admin privileges.

    Raises:
        AdminStateUnknownError if user privileges cannot be determined.
    """
    try:
        return os.getuid() == 0
    except AttributeError:
        pass
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() == 1
    except AttributeError:
        raise AdminStateUnknownError


def getCurrentPath():
    if getattr(sys, 'frozen', False):
        # frozen
        dir_ = os.path.dirname(sys.executable)
    else:
        # unfrozen
        dir_ = os.path.dirname(os.path.realpath(__file__))
    return dir_


if __name__ == '__main__':
    if not isUserAdmin():
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, getCurrentPath(), None, 1)
    app = QApplication(sys.argv)
    ex = Settings()
    ex.show()
    sys.exit(app.exec_())
