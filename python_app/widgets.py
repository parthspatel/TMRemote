import math

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from backend.log import LogThread
from resources.magicNumbers import MagicNumbers as Magic


class Widgets(object):

    class BotLogging(QWidget):
        def __init__(self):

            super().__init__()
            self.__initElements()

        def __initElements(self):
            self.botLoggingCheckBox = QCheckBox('Bot Logging', self)
            self.botLoggingCheckBox.setChecked(True)

            grid = QGridLayout()
            grid.setSpacing(1)

            grid.addWidget(self.botLoggingCheckBox, 0, 0)

            self.setLayout(grid)

    class Maintenance(QWidget):
        def __init__(self):
            super().__init__()
            self.__initElements()

        def __initElements(self):
            self.crashCheckBox = QCheckBox('Crash Clients', self)

            self.restartCheckBox = QCheckBox('Restart PC', self)

            grid = QGridLayout()
            grid.setSpacing(1)

            grid.addWidget(self.crashCheckBox, 1, 0)
            grid.addWidget(self.restartCheckBox, 1, 1)

            self.setLayout(grid)

    class BanDetection(QWidget):

        class WorldCheckBox(QWidget):
            def __init__(self, world=''):
                super().__init__()
                self.__initElements(world)

            def __initElements(self, world):
                self.worldCheckBox = QCheckBox(world, self)
                self.setState('disabled')

            def setState(self, state):

                if 'off' in state:
                    self.setStyleSheet('''
                        QCheckBox:indicator { width: 20px; height: 20px; }
                        QCheckBox:indicator:checked { background-color: #E64C3C;
                                                      border-color: black;
                                                      border-radius: 10px;
                                                      border: 2px solid black; }
                        QCheckBox:indicator:unchecked { background-color: #E64C3C;
                                                        border-radius: 10px;
                                                        border: 2px solid grey;
                                                        opacity: 127 } ''')

                elif 'on' in state:
                    self.setStyleSheet('''
                        QCheckBox:indicator { width: 20px; height: 20px; }
                        QCheckBox:indicator:checked { background-color: #EFE4F2;
                                                      border-color: black;
                                                      border-radius: 10px;
                                                      border: 2px solid black; }
                        QCheckBox:indicator:unchecked { background-color: #EFE4F2;
                                                        border-radius: 10px;
                                                        border: 2px solid grey;
                                                        opacity: 127 } ''')

                elif 'maint' in state:
                    self.setStyleSheet('''
                        QCheckBox:indicator { width: 20px; height: 20px; }
                        QCheckBox:indicator:checked { background-color: #F0C419;
                                                      border-color: black;
                                                      border-radius: 10px;
                                                      border: 2px solid black; }
                        QCheckBox:indicator:unchecked { background-color: #F0C419;
                                                        border-radius: 10px;
                                                        border: 2px solid grey;
                                                        opacity: 127 } ''')

                elif 'disable' in state:
                    self.setStyleSheet('''
                        QCheckBox:indicator { width: 20px; height: 20px; }
                        QCheckBox:indicator:checked { background-color: #FFFFFF;
                                                      border-color: black;
                                                      border-radius: 10px;
                                                      border: 2px solid black; }
                        QCheckBox:indicator:unchecked { background-color: #FFFFFF;
                                                        border-radius: 10px;
                                                        border: 2px solid grey;
                                                        opacity: 127 } ''')

                else:
                    self.setStyleSheet('''
                        QCheckBox:indicator { width: 20px; height: 20px; }
                        QCheckBox:indicator:checked { background-color: pink;
                                                      border-color: white;
                                                      border-radius: 10px;
                                                      border: 2px solid black; }
                        QCheckBox:indicator:unchecked { background-color: pink;
                                                        border-radius: 10px;
                                                        border: 2px solid grey;
                                                        opacity: 127 } ''')

            def isChecked(self):
                return self.worldCheckBox.isChecked()

            def setChecked(self, value):
                self.worldCheckBox.setChecked(value)

            def text(self):
                return self.worldCheckBox.text()

            def stateChanged(self, func):
                self.worldCheckBox.stateChanged.connect(func)

        def __init__(self):
            super().__init__()
            self.__initElements()

        def __initElements(self):
            self.banDetectionCheckBox = QCheckBox('Ban Detection', self)
            self.banDetectionCheckBox.setChecked(True)

            self.allWorldsCheckBox = QCheckBox('All worlds', self)
            self.allWorldsCheckBox.stateChanged.connect(self._tickAllWorlds)

            self.setStyleSheet(''' QCheckBox:indicator { width: 20px; height: 20px; }
                                   QCheckBox:indicator:checked { background-color: #EB5202;
                                                                 border-color: black;
                                                                 border-radius: 10px;
                                                                 border: 2px solid black; }
                                   QCheckBox:indicator:unchecked { background-color: #DEE2E6;
                                                                   border-radius: 10px;
                                                                   border: 2px solid grey; } ''')

            self.worldCheckBoxes = {}
            for world in Magic.WORLDS:
                self.worldCheckBoxes.update(
                    {world.lower(): self.WorldCheckBox(world)})

            grid = QGridLayout()
            grid.setSpacing(2)
            grid.setVerticalSpacing(30)
            grid.addWidget(self.banDetectionCheckBox, 1, 0)
            grid.addWidget(self.allWorldsCheckBox, 1, 1)
            grid.addWidget(self.worldCheckBoxes[Magic.WORLDS[0].lower()], 2, 0)
            grid.addWidget(self.worldCheckBoxes[Magic.WORLDS[1].lower()], 3, 0)
            grid.addWidget(self.worldCheckBoxes[Magic.WORLDS[2].lower()], 4, 0)
            grid.addWidget(self.worldCheckBoxes[Magic.WORLDS[3].lower()], 5, 0)
            grid.addWidget(self.worldCheckBoxes[Magic.WORLDS[4].lower()], 6, 0)
            grid.addWidget(self.worldCheckBoxes[Magic.WORLDS[5].lower()], 2, 1)
            grid.addWidget(self.worldCheckBoxes[Magic.WORLDS[6].lower()], 3, 1)
            grid.addWidget(self.worldCheckBoxes[Magic.WORLDS[7].lower()], 4, 1)
            grid.addWidget(self.worldCheckBoxes[Magic.WORLDS[8].lower()], 5, 1)

            self.setLayout(grid)

        def _tickAllWorlds(self):
            for worldName in self.worldCheckBoxes:
                self.worldCheckBoxes[worldName].setChecked(
                    self.allWorldsCheckBox.isChecked())

    class TMRLogging(QWidget):
        def __init__(self):
            super().__init__()
            self.__initElements()

        def __initElements(self):
            self.logs = QTextEdit()
            self.logs.setReadOnly(True)
            self.logs.setTextInteractionFlags(Qt.NoTextInteraction)

            grid = QGridLayout()
            grid.setSpacing(1)
            grid.addWidget(self.logs, 0, 0)
            self.setLayout(grid)

        def post(self, time, msg):
            logThread = LogThread()
            logThread.post(time, msg)
            signal = logThread.getSignal()
            signal.connect(self.__post)
            logThread.start()
            logThread.quit()

        def __post(self, time, msg):
            if list is type(msg):
                for each in msg:
                    self.logs.append(f'{time}: {each}')
            else:
                self.logs.append(f'{time}: {msg}')
