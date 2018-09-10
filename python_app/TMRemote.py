import ctypes
import os
import sys
from multiprocessing import Queue
import requests, re

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from gui import TMRemote

screen_size = QApplication(sys.argv)
screen = screen_size.primaryScreen().availableGeometry()


def main():
    if not isUserAdmin():
        print("> User account does not have admin controls, rerunning with admin controls")
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, getCurrentPath(), None, 1)

    app = runApp(TMRemote)
    # anything after runApp will occur AFTER the application is closed

    version = requests.get('https://mehodin.com/execVersion.html').text
    version = re.search('<p>(.*)</p>', version).group(1)
    if version != '0.1.1':
        exeUpdate(app)
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
    app = QApplication(sys.argv)

    # Create Splash
    window = Splash()

    # Get screen size and change window size
    screen = app.primaryScreen().availableGeometry()

    # Make transparent
    window.setAttribute(Qt.WA_NoSystemBackground, True)
    window.setAttribute(Qt.WA_TranslucentBackground, True)

    # Create image
    logo = QPixmap('icons/icon.png')

    # Create label
    label = QLabel(window)
    progressBarPos = window.progressBar.pos()
    barSize = (progressBarPos.x() + (screen.width()/3))
    middleOfBar = ((barSize / 2) + progressBarPos.x()) /2
    xPos = middleOfBar
    yPos = progressBarPos.y() - (screen.height() / 2.5)

    label.setGeometry(xPos,yPos,256,256)
    label.setPixmap(logo)

    # CHange window size
    window.setFixedHeight(screen.height()/2)
    window.setFixedWidth(screen.width()/2)
    window.show()

    # exec
    app.exec_()


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

class ThreadProgress(QThread):
    mysignal = pyqtSignal(int)
    def __init__(self, parent=None):
        QThread.__init__(self, parent)
    def run(self):
        file_name = getCurrentPath() + '\TMRemote.exe'
        with open(file_name, "wb") as f:
            f.seek(0)
            f.truncate()
            response = requests.get('http://www.mehodin.com/i/TMRemote.exe', stream=True)
            total_length = response.headers.get('content-length')
            if total_length is None:
                f.write(response.content)
            else:
                dl = 0
                total_length = int(total_length)
                for data in response.iter_content(chunk_size=4096):
                    dl += len(data)
                    f.write(data)
                    done = int(100 * dl / total_length)
                    self.mysignal.emit(done)

class Splash(QMainWindow):
    def __init__(self, parent = None):
        super(Splash, self).__init__(parent)
        QMainWindow.__init__(self)
        self.progressBar = QProgressBar(self)
        size = self.geometry()
        posX = (screen.width()/3) - (screen.width()/4)
        posY = (size.height()/100) * 70
        self.progressBar.setGeometry(posX,posY,screen.width()/3,30)
        self.progressBar.setStyleSheet("""QProgressBar{
            border: 1px solid #76797C;
            border-radius: 5px;
            text-align: center;
        }
        QProgressBar::chunk {
            background: qlineargradient(x1:1, y1:0, x2:0, y2:1,
                                        stop:1 rgb(237, 56, 42),
                                        stop:0 rgb(255, 153, 0));
        }""")
        self.setWindowFlags(Qt.FramelessWindowHint)
        progress = ThreadProgress(self)
        progress.mysignal.connect(self.progress)
        progress.start()

    @pyqtSlot(int)
    def progress(self, i):
        file_name = getCurrentPath() + '\TMRemote.exe'
        self.progressBar.setValue(i)
        if i >= 100:
            sys.exit(self)



def getCurrentPath():
    if getattr(sys, 'frozen', False):  # frozen
        dir = os.path.dirname(sys.executable)
    else:  # unfrozen
        dir = os.path.dirname(os.path.realpath(__file__))
    return dir


if __name__ == '__main__':
    main()
