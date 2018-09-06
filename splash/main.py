from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import os
import sys
import time
import requests

link = 'https://mehodin.com/i/source.rar'
file_name = "download.rar"
screen_size = QApplication(sys.argv)
screen = screen_size.primaryScreen().availableGeometry()

class ThreadProgress(QThread):
    mysignal = pyqtSignal(int)
    def __init__(self, parent=None):
        QThread.__init__(self, parent)
    def run(self):
        with open(file_name, "wb") as f:
            response = requests.get(link, stream=True)
            total_length = response.headers.get('content-length')

            if total_length is None: # no content length header
                f.write(response.content)
            else:
                dl = 0
                total_length = int(total_length)
                for data in response.iter_content(chunk_size=4096):
                    dl += len(data)
                    f.write(data)
                    done = int(100 * dl / total_length)
                    self.mysignal.emit(done)
        sys.exit()

FROM_SPLASH,_ = loadUiType(os.path.join(os.path.dirname(__file__),"splash.ui"))


class Splash(QMainWindow, FROM_SPLASH):
    def __init__(self, parent = None):
        super(Splash, self).__init__(parent)
        QMainWindow.__init__(self)
        screenHeight = screen.height()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        progress = ThreadProgress(self)
        progress.mysignal.connect(self.progress)
        progress.start()

    @pyqtSlot(int)
    def progress(self, i):
        self.progressBar.setValue(i)
        self.frameGeometry().width(), self.frameGeometry().height()
        posX = (screen.width()/3) - (screen.width()/4)
        posY = (5 * (screen.height()/8)) #+ (screen.height()-(screen.height()/2))# + 200
        self.progressBar.setGeometry(posX,posY,screen.width()/3,30)
        if i == 100:
            self.hide()
            os.startfile(file_name)


def main():
    app = QApplication(sys.argv)
    window = Splash()
    screen = app.primaryScreen().availableGeometry()
    window.setFixedHeight(screen.height()/2)
    window.setFixedWidth(screen.width()/2)
    window.setStyleSheet('QSplashScreen {opacity:0}')
    window.show()
    app.exec_()

if __name__ == '__main__':
    try:
        main()
    except Exception as why:
        print(why)
