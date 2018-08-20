import time

import pyautogui
import win32gui


class ClientLauncher(object):
    def __init__(self):
        self.processName = 'terminalmanager'
        self.repeatCount = 4000 // pyautogui.size()[1]

    def __windowEnumerationHandler(self, hwnd, top_windows):
        top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

    def __GetTerminalManagerWindow(self):
        results = []
        top_windows = []
        win32gui.EnumWindows(self.__windowEnumerationHandler, top_windows)
        for i in top_windows:
            if self.processName in i[1].lower():
                win32gui.ShowWindow(i[0], 5)
                win32gui.SetForegroundWindow(i[0])
                break

    def __GetInCurrentWindow(self):
        self.__GetTerminalManagerWindow()
        checkboxArray = list(pyautogui.locateAllOnScreen(
            'checkbox.png'))
        for Checkbox in checkboxArray:
            for index in range(0, len(checkboxArray)):
                pyautogui.keyDown('ctrl')
                pyautogui.click(
                    checkboxArray[index][0] + 30, checkboxArray[index][1])
            pyautogui.rightClick(checkboxArray[0][0], checkboxArray[0][1])
            pyautogui.moveRel(10, 10)
            pyautogui.click()
            break
        pyautogui.keyUp('ctrl')

    def launchClients(self):
        if self.repeatCount < 1:
            self.repeatCount = 1
        for count in range(self.repeatCount):
            self.__GetInCurrentWindow()
            pyautogui.scroll(-pyautogui.size()[1])
