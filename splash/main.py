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
            f.seek(0)
            f.truncate()
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
        self.progressBar.setValue(i)
        if i >= 100:
            self.hide()
            os.startfile(file_name)


def main():
    app = QApplication(sys.argv)

    # Create Splash
    window = Splash()

    # Get screen size and change window size
    screen = app.primaryScreen().availableGeometry()

    # Make transparent
    window.setAttribute(Qt.WA_NoSystemBackground, True)
    window.setAttribute(Qt.WA_TranslucentBackground, True)

    # Create image
    logo = QPixmap('icon.png')

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

if __name__ == '__main__':
    main()
