from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from resources.magicNumbers import MagicNumbers as Magic


class TMRemote(QMainWindow):

    def __init(self):
        super().__init__()

        self.__initProperties()
        self.__initGUI()

    def __initProperties(self):
        self.title = 'Terminal Manager Remote'

        QCoreApplication.setOrganizationName("TMRemote")
        QCoreApplication.setOrganizationDomain("TMRemote.io")
        QCoreApplication.setApplicationName("TMRemote")
        QCoreApplication.setApplicationVersion('0.0.1')

        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480

    def __initGUI(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon('resources\icon.ico'))
        self.setGeometry(self.left,
                         self.top,
                         self.width,
                         self.height)

    def __initMenuBar(self):
        # Main Menu bar
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        editMenu = mainMenu.addMenu('Edit')

        # File Menu
        # ---------------------------------------------------------------------
        # Refresh (F5)
        refreshButton = QAction(QIcon('icons\\refresh.svg'), 'Refresh', self)
        refreshButton.setShortcut('F5')
        refreshButton.triggered.connect(self.update)
        fileMenu.addAction(refreshButton)

        # Exit (ctrl + Q)
        exitButton = QAction(QIcon('icons\exit.svg'), 'Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)

        # Edit Menu
        # ---------------------------------------------------------------------
        # Settings
        settingsButton = QAction(QIcon('icons\settings.svg'), 'Settings', self)
        settingsButton.triggered.connect(self.onPushSettings)
        editMenu.addAction(settingsButton)
