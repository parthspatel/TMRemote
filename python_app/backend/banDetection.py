import ast
import os
import pickle

from PyQt5.QtCore import QThread

from backend.auth import Auth
from backend.log import Log


class BanDetectionThread(QThread):
    def __init__(self, username, password, api_key, tm_path, banDetectionWidget, logs, links):
        QThread.__init__(self)
        self.get_username = username
        self.get_password = password
        self.api_key = api_key

        self.get_tm_path = tm_path

        self.banDetectionCheckBox = banDetectionWidget.banDetectionCheckBox
        self.allWorldsCheckBox = banDetectionWidget.allWorldsCheckBox
        self.worldCheckBoxes = banDetectionWidget.worldCheckBoxes

        self.logs = logs
        self.links = links

        self.sleep_time = 60
        self.sleep_time_const = self.sleep_time
        self.prevBanDetection = {}

        self.noAccessMessage = 'Please upgrade your license to gain access to ban detection'
        self.checkBoxGreyscale = '''
                                   QCheckBox:indicator {width: 20px; height: 20px;}
                                   QCheckBox:indicator:checked { background-color: #2ecc71;
                                                                 border-color: black;
                                                                 border-radius: 10px;
                                                                 border: 2px solid black;}
                                   QCheckBox:indicator:unchecked { background-color: #DEE2E6;
                                                                   border-radius: 10px;
                                                                   border: 2px solid grey;} '''

    def __del__(self):
        self.wait()

    def get_tmremote_folder(self):
        return self.get_tm_path().split('TerminalManager.exe')[0] + 'TMRemote'

    def __isEnabled(self):
        if not self.banDetectionCheckBox.isChecked():
            try:
                os.remove(self.get_tmremote_folder() + '/temp/banDetectStatus')
            except:
                pass
            return False
        else:
            return True

    @Auth.authenticate(level='prime')
    def __getBanDetection(self, token):
        return token

    @Log.log
    def parseBanDetection(self):
        gmStatus = self.__getBanDetection()
        if not gmStatus:
            return f'Ban Status Failed Auth: {gmStatus}'
        try:
            GMLogs = gmStatus.json()
        except SyntaxError:
            pass
        if 'fail' in gmStatus.lower():
            self.banDetectionCheckBox.setEnabled(False)
            self.banDetectionCheckBox.setToolTip(self.noAccessMessage)
            self.allWorldsCheckBox.setEnabled(False)
            self.allWorldsCheckBox.setToolTip(self.noAccessMessage)
            for world in self.worldCheckBoxes:
                self.worldCheckBoxes[world].setEnabled(False)
                self.worldCheckBoxes[world].setToolTip(self.noAccessMessage)
                self.worldCheckBoxes[world].setState('disabled')
                self.worldCheckBoxes[world].setStyleSheet(
                    self.checkBoxGreyscale)
            self.banDetectionCheckBox.setStyleSheet(self.checkBoxGreyscale)
            return gmStatus
        if not self.banDetectionCheckBox.isEnabled():
            self.banDetectionCheckBox.setEnabled(True)
            self.allWorldsCheckBox.setEnabled(True)
            self.banDetectionCheckBox.setStyleSheet('''
                                   QCheckBox: indicator {width: 20px; height: 20px; }
                                   QCheckBox: indicator: checked {background-color:  # 2ecc71;
                                                                 border-color: black;
                                                                 border-radius: 10px;
                                                                 border: 2px solid black;}
                                   QCheckBox: indicator: unchecked {background-color:  # DEE2E6;
                                                                   border-radius: 10px;
                                                                   border: 2px solid grey;} ''')
            # background-color: #EB5202;

            for world in GMLogs['worlds']:
                if GMLogs['worlds'][world]['status'] == self.prevBanDetection.get(world):
                    continue
                self.worldCheckBoxes[world.lower()].setState(
                    GMLogs['worlds'][world]['status'])

        gm_status = []
        for world in GMLogs['worlds']:
            if GMLogs['worlds'][world]['status'] == self.prevBanDetection.get(world):
                continue
            self.worldCheckBoxes[world.lower()].setState(
                GMLogs['worlds'][world]['status'])

            gm_status.append('BD Status: {} in {}'.format(
                GMLogs['worlds'][world]['status'], GMLogs['worlds'][world]['name']))
            self.prevBanDetection[world] = GMLogs['worlds'][world]['status']

        try:
            if self.get_tmremote_folder():
                if not os.path.exists(self.get_tmremote_folder() + '/temp'):
                    os.makedirs(self.get_tmremote_folder() + '/temp')
                with open(self.get_tmremote_folder() + '/temp/banDetectStatus', 'wb+') as file:
                    pickle.dump(str(GMLogs), file)
            else:
                return
        except Exception as ex:
            return f'Could not access TMRemote folder: {ex}'

        if not self.prevBanDetection:
            self.prevBanDetection = GMLogs

        return gm_status

    def run(self):
        while True:
            if self.__isEnabled():
                self.parseBanDetection()
                self.sleep(self.sleep_time)
            self.sleep(1)
