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

        self.__init_properties()
        self.__init__gui()
        self.settings_window = Settings(self)

        self.startEvent()

        self.thread = MainThread(
            username=self.settings_window.get_username,
            password=self.settings_window.get_password,
            api_key={
                'get': self.get_api_key,
                'set': self.set_api_key},
            profilesDir=self.settings_window.getProfileDir,
            tm_path=self.settings_window.get_tm_path,
            banDetectionWidget=self.banDetectionWidget,
            maintenanceWidget=self.maintenanceWidget,
            logs=self.tmrLoggingWidget,
            generalSettingsWidget=self.generalSettingsWidget,
            settingsTextEdits=self.settings_window.getTextEdits())
        self.thread.start()

    def __init_properties(self):
        self.title = 'Terminal Manager Remote'

        QCoreApplication.setOrganizationName("TMRemote")
        QCoreApplication.setOrganizationDomain("TMRemote.io")
        QCoreApplication.setApplicationName("TMRemote")
        QCoreApplication.setApplicationVersion('0.0.0.1')

        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480

    def __init__gui(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon(r'.\icons\icon.ico'))
        self.setGeometry(self.left,
                         self.top,
                         self.width,
                         self.height)

        self.__initMenuBar()

        self.generalSettingsWidget = Widgets.generalSettings()
        self.maintenanceWidget = Widgets.Maintenance()
        self.banDetectionWidget = Widgets.BanDetection()
        self.tmrLoggingWidget = Widgets.TMRLogging()

        self.set_api_key()

        self.__initTabs()

    def __initMenuBar(self):
        # Main Menu bar
        main_menu = self.menuBar()
        file_menu = main_menu.addMenu('File')
        edit_menu = main_menu.addMenu('Edit')

        # File Menu
        # ---------------------------------------------------------------------
        # Refresh (F5)
        refreshButton = QAction(
            QIcon(r'.\icons\refresh.svg'), 'Refresh', self)
        refreshButton.setShortcut('F5')
        refreshButton.triggered.connect(self.update)
        file_menu.addAction(refreshButton)

        # Exit (ctrl + Q)
        exit_button = QAction(QIcon(r'.\icons\exit.svg'), 'Exit', self)

        exit_button.setShortcuts([QKeySequence('Ctrl+Q'),
                                  QKeySequence('Alt+F4')])
        exit_button.setStatusTip('Exit application')
        exit_button.triggered.connect(self.close)
        file_menu.addAction(exit_button)

        # Edit Menu
        # ---------------------------------------------------------------------
        # Settings
        settings_button = QAction(
            QIcon(r'.\icons\settings.svg'), 'Settings', self)
        settings_button.triggered.connect(self.__onPushSettings)
        edit_menu.addAction(settings_button)

    def __onPushSettings(self):
        self.update()
        self.settings_window.update()
        self.settings_window.show()

    def __initTabs(self):

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        mainBox = QVBoxLayout()
        tabWidget = QTabWidget()

        generalSettingBox = QGroupBox('General Settings')
        maintenanceBox = QGroupBox('Game Maintenance Settings')
        banDetectionBox = QGroupBox('Ban Detection Settings')
        tmrLoggingBox = QGroupBox('TMRemote Logs')

        hbox_temp = QHBoxLayout()
        hbox_temp.addWidget(self.generalSettingsWidget)
        generalSettingBox.setLayout(hbox_temp)

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
        settingsTab.layout.addWidget(generalSettingBox)
        settingsTab.setLayout(settingsTab.layout)

        mainBox.addWidget(tabWidget)
        centralWidget.setLayout(mainBox)

    def set_api_key(self, key=None):
        self.api_key = key
        self.update()

    def get_api_key(self):
        return self.api_key

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
            if self.settings_window.get_tm_path() and self.settings_window.get_tm_path().strip():
                if not self.__processExists('TerminalManager'):
                    # Get TMR current path
                    tmr_dir = os.path.dirname(
                        os.path.realpath(getCurrentPath()))

                    # Let TMR load, then start Terminal Manager
                    time.sleep(0.3)
                    os.chdir(self.settings_window.get_tm_path().split(
                        'TerminalManager.exe')[0])
                    os.start(self.settings_window.get_tm_path())
                    time.sleep(0.1)
                    os.chdir(tmr_dir)
        except BaseException:
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

        self.settings_window.setUsername(
            settings.value('username'))
        self.settings_window.setPassword(
            settings.value('password'))
        self.settings_window.setProfileDir(settings.value('profileDir'))
        self.settings_window.settm_path(settings.value('tm_path'))

        self.set_api_key(settings.value('api_key'))

        for world in Magic.WORLDS:
            checked = False if None is settings.value(
                world.lower()) or 'false' in settings.value(
                world.lower()).lower() else True
            self.banDetectionWidget.worldCheckBoxes[world.lower()].setChecked(
                checked)

        self.banDetectionWidget.banDetectionCheckBox.setChecked(False if None is settings.value(
            'banDetection') or 'false' in settings.value('banDetection').lower() else True)

        self.maintenanceWidget.crashCheckBox.setChecked(False if None is settings.value(
            'crashMaint') or 'false' in settings.value('crashMaint').lower() else True)
        self.maintenanceWidget.restartCheckBox.setChecked(False if None is settings.value(
            'restartMaint') or 'false' in settings.value('restartMaint').lower() else True)
        self.generalSettingsWidget.startManagerCheckBox.setChecked(False if None is settings.value(
            'startManager') or 'false' in settings.value('startManager').lower() else True)

        settings.endGroup()

    def __writeSettings(self):
        settings = QSettings()

        settings.beginGroup('windowSettings')
        settings.setValue("geometry", self.saveGeometry())
        settings.setValue("saveState", self.saveState())
        settings.setValue("maximized", self.isMaximized())
        if not self.isMaximized():
            settings.setValue("pos", self.pos())
            settings.setValue("size", self.size())

        for world in Magic.WORLDS:
            value = bool(
                self.banDetectionWidget.worldCheckBoxes[world.lower()].isChecked())
            settings.setValue(world.lower(), value)

        vars = {
            'username': self.settings_window.get_username(),
            'password': self.settings_window.get_password(),
            'api_key': self.get_api_key(),
            'profileDir': self.settings_window.getProfileDir(),
            'tm_path': self.settings_window.get_tm_path(),
            'banDetection': bool(
                self.banDetectionWidget.banDetectionCheckBox.isChecked()),
            'crashMaint': bool(
                self.maintenanceWidget.crashCheckBox.isChecked()),
            'restartMaint': bool(
                self.maintenanceWidget.restartCheckBox.isChecked()),
            'startManager': bool(
                self.generalSettingsWidget.startManagerCheckBox.isChecked())}

        for key, value in vars.items():
            settings.setValue(key, value)

        settings.endGroup()

    def __closeThreads(self):
        self.thread.quit()

    def __get_tmremote_dir(self):
        return self.settings_window.get_tm_path().replace(
            'TerminalManager.exe', 'TMRemote')

    def __removeTempFiles(self):
        tempDir = self.__get_tmremote_dir() + '/temp'
        for file in os.listdir(tempDir):
            try:
                os.remove(os.path.join(tempDir, file))
            except BaseException:
                pass


def getCurrentPath():
    if getattr(sys, 'frozen', False):  # frozen
        dir = os.path.dirname(sys.executable)
    else:  # unfrozen
        dir = os.path.dirname(os.path.realpath(__file__))
    return dir
