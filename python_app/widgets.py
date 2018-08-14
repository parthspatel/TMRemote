import math

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

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

                self.pixmap_off = QPixmap(r'.\resources\server_state_off_16.svg')
                self.pixmap_on = QPixmap(r'.\resources\server_state_on_16.svg')
                self.pixmap_loading = QPixmap(r'.\resources\server_state_loading_16.svg')
                self.pixmap_disabled = QPixmap(r'.\resources\server_state_disabled_16.svg')

                self.__initElements(world)

            def __initElements(self, world):
                self.worldCheckBox = QCheckBox(world, self)

                self.state = QLabel(self)
                self.setState('disabled')

                self.worldCheckBox.move(self.state.x() + self.state.height(),
                                        self.state.y())

                self.state.move(self.state.x(), self.state.y() + 3)

            def setState(self, state):

                if 'off' in state:
                    self.state.setPixmap(self.pixmap_off)
                elif 'on' in state:
                    self.state.setPixmap(self.pixmap_on)
                elif 'maint' in state:
                    self.state.setPixmap(self.pixmap_loading)
                elif 'disable' in state:
                    self.state.setPixmap(self.pixmap_disabled)
                else:
                    self.state.setPixmap(self.pixmap_disabled)

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

            self.worldCheckBoxes = {}
            for world in Magic.WORLDS:
                self.worldCheckBoxes.update({world.lower(): self.WorldCheckBox(world)})

            grid = QGridLayout()
            grid.setSpacing(1)
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
            for worldCheckBox in self.worldCheckBoxes:
                checkbox.setChecked(self.allWorldsCheckBox.isChecked())

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
