import os
import sys
import time
import zipfile
from multiprocessing import Queue

import requests
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType

screen_size = QApplication(sys.argv)
screen = screen_size.primaryScreen().availableGeometry()


class ThreadProgress(QThread):
    mysignal = pyqtSignal(int)

    def __init__(self, terminalManager, installPath, parent=None):
        QThread.__init__(self)
        self.terminalManager = terminalManager
        self.installPath = installPath + '/TMRemote'
        self.link = 'https://mehodin.com/i/TMRemote.zip'
        self.tmrFolder = None

    def __createFolder(self, folderPath):
        if not os.path.isdir(folderPath):
            os.mkdir(folderPath)

    def __folderCheck(self):
        self.tmrFolder = self.terminalManager + '/TMRemote'
        scriptsFolder = self.tmrFolder + '/Scripts'
        tempFolder = self.tmrFolder + '/temp'
        self.__createFolder(self.tmrFolder)
        self.__createFolder(scriptsFolder)
        self.__createFolder(tempFolder)

    def __downloadScript(self):
        tmPath = self.terminalManager
        scriptPath = tmPath + '/TMRemote/Scripts/Logger.py'
        try:
            scriptContent = requests.get(
                'https://mehodin.com/i/Logger.py').text
            try:
                os.remove(scriptPath)
            except FileNotFoundError:
                pass
            with open(scriptPath, 'w') as script:
                script.write(scriptContent)
            return True
        except Exception as e:
            return False

    def __downloadModule(self):
        tmPath = self.terminalManager
        modulePath = tmPath + '/TMRemote/Scripts/TMRLogger.pyc'
        try:
            moduleContent = requests.get(
                'https://mehodin.com/i/TMRLogger.pyc').content
            try:
                os.remove(modulePath)
            except FileNotFoundError:
                pass
            with open(modulePath, 'wb') as moduleFile:
                moduleFile.write(moduleContent)
            return True
        except Exception as e:
            return False

    def run(self):
        self.__folderCheck()
        self.downloadPathExe = self.tmrFolder + '/temp/TMRemote.zip'
        with open(self.downloadPathExe, "wb+") as f:
            f.seek(0)
            f.truncate()
            response = requests.get(self.link, stream=True)
            total_length = response.headers.get('content-length')
            if total_length is None:
                f.write(response.content)
            else:
                dl = 0
                total_length = int(total_length)
                for data in response.iter_content(chunk_size=4096):
                    dl += len(data)
                    f.write(data)
                    done = int(97 * dl / total_length)
                    self.mysignal.emit(done)
                self.__createFolder(self.installPath)
        zip_ref = zipfile.ZipFile(self.downloadPathExe, 'r')
        zip_ref.extractall(self.installPath)
        zip_ref.close()
        if os.path.isfile(self.downloadPathExe):
            os.remove(self.downloadPathExe)
        done += 1
        self.mysignal.emit(done)
        self.__downloadScript()
        done += 1
        self.mysignal.emit(done)
        self.__downloadModule()
        done += 1
        self.mysignal.emit(done)


class Splash(QMainWindow):
    def __init__(self, parent=None):
        super(Splash, self).__init__(parent)
        QMainWindow.__init__(self)

        self.setWindowOpacity(0.1)
        self.setStyleSheet("QWidget{background: #fff}")

        self.progressBar = QProgressBar(self)
        size = self.geometry()
        posX = (screen.width()/3) - (screen.width()/4)
        posY = (size.height()/100) * 70
        self.progressBar.setGeometry(posX, posY, screen.width()/3, 30)
        self.progressBar.setStyleSheet("""QProgressBar{
            border: 1px solid #76797C;
            border-radius: 5px;
            text-align: center;
        }
        QProgressBar::chunk {
            background: qlineargradient(x1:0, y1:1, x2:1, y2:0,
                                        stop:1 rgb(237, 56, 42),
                                        stop:0 rgb(255, 153, 0));
        }""")
        self.setWindowFlags(Qt.FramelessWindowHint)
        installPath = QFileDialog.getExistingDirectory(
            self, "Please select where you would like to install TMRemote")
        if len(installPath) is 0:
            sys.exit()
        terminalManager = QFileDialog.getExistingDirectory(
            self, "Please select where your Terminal Manager folder is")
        if len(terminalManager) is 0:
            sys.exit()
        self.progressThread = ThreadProgress(terminalManager, installPath)
        self.progressThread.mysignal.connect(self.progress)
        self.progressThread.start()

    def __del__(self):
        pass

    @pyqtSlot(int)
    def progress(self, i):
        self.progressBar.setValue(i)
        if i >= 100:
            sys.exit()


def main():
    app = QApplication(sys.argv)

    # Create Splash
    window = Splash()

    # Get screen size and change window size
    screen = app.primaryScreen().availableGeometry()

    # Create image
    logo = QPixmap('icons\icon.svg')

    # Create label
    label = QLabel(window)
    progressBarPos = window.progressBar.pos()
    barSize = (progressBarPos.x() + (screen.width()/3))

    middleOfBar = (barSize - 256 + progressBarPos.x()) / 2

    xPos = middleOfBar
    yPos = progressBarPos.y() - (screen.height() / 2.5)

    label.setGeometry(xPos, yPos, 256, 256)
    label.setPixmap(logo)

    # CHange window size
    window.setFixedHeight(screen.height()/2)
    window.setFixedWidth(screen.width()/2)
    window.show()

    # exec
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
