import base64
import os
import sys
import time
from multiprocessing import Queue

import psutil
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from backend.mainThread import MainThread
from resources.magicNumbers import MagicNumbers as Magic
from settings import Settings
from widgets import Widgets


class TMRemote(QMainWindow):

    def __init__(self):
        super().__init__()

        self.__initProperties()
        self.__initGUI()
        self.settingsWindow = Settings(self)

        self.startEvent()

        self.thread = MainThread(username=self.settingsWindow.getUsername,
                                 password=self.settingsWindow.getPassword,
                                 apikey=self.settingsWindow.getAPIKey,
                                 profilesDir=self.settingsWindow.getProfileDir,
                                 tmPath=self.settingsWindow.getTMPath,
                                 banDetectionWidget=self.banDetectionWidget,
                                 maintenanceWidget=self.maintenanceWidget,
                                 logs=self.tmrLoggingWidget)
        self.thread.start()

    def __initProperties(self):
        self.title = 'Terminal Manager Remote'

        QCoreApplication.setOrganizationName("TMRemote")
        QCoreApplication.setOrganizationDomain("TMRemote.io")
        QCoreApplication.setApplicationName("TMRemote")
        QCoreApplication.setApplicationVersion('0.0.0.1')

        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480

    def __initGUI(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon(r'.\icons\icon.ico'))
        self.setGeometry(self.left,
                         self.top,
                         self.width,
                         self.height)

        self.__initMenuBar()

        self.botLogggingWidget = Widgets.BotLogging()
        self.maintenanceWidget = Widgets.Maintenance()
        self.banDetectionWidget = Widgets.BanDetection()
        self.tmrLoggingWidget = Widgets.TMRLogging()

        self.__initTabs()

    def __initMenuBar(self):
        # Main Menu bar
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        editMenu = mainMenu.addMenu('Edit')

        # File Menu
        # ---------------------------------------------------------------------
        # Refresh (F5)
        refreshButton = QAction(
            QIcon(r'.\icons\refresh.svg'), 'Refresh', self)
        refreshButton.setShortcut('F5')
        refreshButton.triggered.connect(self.update)
        fileMenu.addAction(refreshButton)

        # Exit (ctrl + Q)
        exitButton = QAction(QIcon(r'.\icons\exit.svg'), 'Exit', self)

        exitButton.setShortcuts([QKeySequence('Ctrl+Q'),
                                 QKeySequence('Alt+F4')])
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)

        # Edit Menu
        # ---------------------------------------------------------------------
        # Settings
        settingsButton = QAction(
            QIcon(r'.\icons\settings.svg'), 'Settings', self)
        settingsButton.triggered.connect(self.__onPushSettings)
        editMenu.addAction(settingsButton)

    def __onPushSettings(self):
        self.update
        self.settingsWindow.update
        self.settingsWindow.show()

    def __initTabs(self):

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        mainBox = QVBoxLayout()
        tabWidget = QTabWidget()

        botLoggingBox = QGroupBox('Bot Logging Settings')
        maintenanceBox = QGroupBox('Game Maintenance Settings')
        banDetectionBox = QGroupBox('Ban Detection Settings')
        tmrLoggingBox = QGroupBox('TMRemote Logs')

        hbox_temp = QHBoxLayout()
        hbox_temp.addWidget(self.botLogggingWidget)
        botLoggingBox.setLayout(hbox_temp)

        hbox_temp = QHBoxLayout()
        hbox_temp.addWidget(self.maintenanceWidget)
        maintenanceBox.setLayout(hbox_temp)

        hbox_temp = QHBoxLayout()
        hbox_temp.addWidget(self.banDetectionWidget)
        banDetectionBox.setLayout(hbox_temp)

        hbox_temp = QHBoxLayout()
        hbox_temp.addWidget(self.tmrLoggingWidget)
        tmrLoggingBox.setLayout(hbox_temp)

        banDetectionTab = QWidget()
        settingsTab = QWidget()
        tmrLoggingTab = QWidget()

        tabWidget.addTab(banDetectionTab, 'Ban Detection')
        tabWidget.addTab(settingsTab, 'TMRemote')
        tabWidget.addTab(tmrLoggingTab, 'Logs')

        banDetectionTab.layout = QVBoxLayout()
        banDetectionTab.layout.addWidget(banDetectionBox)
        banDetectionTab.setLayout(banDetectionTab.layout)

        tmrLoggingTab.layout = QVBoxLayout()
        tmrLoggingTab.layout.addWidget(tmrLoggingBox)
        tmrLoggingTab.setLayout(tmrLoggingTab.layout)

        settingsTab.layout = QVBoxLayout()
        settingsTab.layout.addWidget(maintenanceBox)
        settingsTab.setLayout(settingsTab.layout)

        mainBox.addWidget(tabWidget)
        centralWidget.setLayout(mainBox)

    def startEvent(self):
        self.__readAndApplySettings()
        # self.__startTerminalManager()

    def closeEvent(self, event=None):
        self.__writeSettings()
        self.__closeThreads()
        self.__removeTempFiles()
        self.close()

    def __startTerminalManager(self):
        try:
            if self.settingsWindow.getTMPath() and self.settingsWindow.getTMPath().strip():
                if not self.__processExists('TerminalManager'):
                    # Get TMR current path
                    tmr_dir = os.path.dirname(
                        os.path.realpath(getCurrentPath()))

                    # Let TMR load, then start Terminal Manager
                    time.sleep(0.3)
                    os.chdir(self.settingsWindow.getTMPath().split(
                        'TerminalManager.exe')[0])
                    os.startfile(self.settingsWindow.getTMPath())
                    time.sleep(0.1)
                    os.chdir(tmr_dir)
        except:
            pass

    def __processExists(self, process_name):
        return bool(process_name in (p.name() for p in psutil.process_iter()))

    def __readAndApplySettings(self):

        settings = QSettings()

        settings.beginGroup('windowSettings')
        self.restoreGeometry(settings.value("geometry", self.saveGeometry()))
        self.restoreState(settings.value("saveState", self.saveState()))
        self.move(settings.value("pos", self.pos()))
        self.resize(settings.value("size", self.size()))

        self.settingsWindow.setUsername(
            settings.value('username'))
        self.settingsWindow.setPassword(
            settings.value('password'))
        self.settingsWindow.setAPIKey(settings.value('apikey'))
        self.settingsWindow.setProfileDir(settings.value('profileDir'))

        self.settingsWindow.setTMPath(settings.value('tmPath'))

        for world in Magic.WORLDS:
            checked = False if None is settings.value(
                world.lower()) or 'false' in settings.value(world.lower()).lower() else True
            self.banDetectionWidget.worldCheckBoxes[world.lower()].setChecked(
                checked)

        self.banDetectionWidget.banDetectionCheckBox.setChecked(False if None is settings.value(
            'banDetection') or 'false' in settings.value('banDetection').lower() else True)

        self.maintenanceWidget.crashCheckBox.setChecked(False if None is settings.value(
            'crashMaint') or 'false' in settings.value('crashMaint').lower() else True)
        self.maintenanceWidget.restartCheckBox.setChecked(False if None is settings.value(
            'restartMaint') or 'false' in settings.value('restartMaint').lower() else True)

        settings.endGroup()

    def __writeSettings(self):
        settings = QSettings()

        settings.beginGroup('windowSettings')
        settings.setValue("geometry", self.saveGeometry())
        settings.setValue("saveState", self.saveState())
        settings.setValue("maximized", self.isMaximized())
        if not self.isMaximized() == True:
            settings.setValue("pos", self.pos())
            settings.setValue("size", self.size())

        for world in Magic.WORLDS:
            value = bool(
                self.banDetectionWidget.worldCheckBoxes[world.lower()].isChecked())
            settings.setValue(world.lower(), value)

        vars = {'username': self.settingsWindow.getUsername(),
                'password': self.settingsWindow.getPassword(),
                'apikey': self.settingsWindow.getAPIKey(),
                'profileDir': self.settingsWindow.getProfileDir(),
                'tmPath': self.settingsWindow.getTMPath(),
                'banDetection': bool(self.banDetectionWidget.banDetectionCheckBox.isChecked()),
                'crashMaint': bool(self.maintenanceWidget.crashCheckBox.isChecked()),
                'restartMaint': bool(self.maintenanceWidget.restartCheckBox.isChecked())}

        for key, value in vars.items():
            settings.setValue(key, value)

        settings.endGroup()

    def __closeThreads(self):
        self.thread.quit()

    def __getTMRemoteDir(self):
        return self.settingsWindow.getTMPath().split('TerminalManager.exe')[0] + 'TMRemote'

    def __removeTempFiles(self):
        tempDir = self.__getTMRemoteDir() + '/temp'
        for file in os.listdir(tempDir):
            try:
                os.remove(os.path.join(tempDir, file))
            except Exception as ex:
                print(f'Error Remove File {file}: {ex}')


def getCurrentPath():
    if getattr(sys, 'frozen', False):  # frozen
        dir = os.path.dirname(sys.executable)
    else:  # unfrozen
        dir = os.path.dirname(os.path.realpath(__file__))
    return dir
