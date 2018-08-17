import datetime
import time
import os
import sys
import pickle
import ast

import GameState
import Character
import Inventory
import Terminal

class Log(object):

    def __init__(self):
        self.LevelToExp = {1: 15, 2: 34, 3: 57, 4: 92, 5: 135, 6: 372, 7: 560, 8: 840, 9: 1242, 10: 1242, 11: 1242, 12: 1242, 13: 1242, 14: 1242, 15: 1490, 16: 1788, 17: 2145, 18: 2574, 19: 3088, 20: 3705, 21: 4446, 22: 5335, 23: 6402, 24: 7682, 25: 9218, 26: 11061, 27: 13273, 28: 15927, 29: 19112, 30: 19112, 31: 19112, 32: 19112, 33: 19112, 34: 19112, 35: 22934, 36: 27520, 37: 33024, 38: 39628, 39: 47553, 40: 51357, 41: 55465, 42: 59902, 43: 64694, 44: 69869, 45: 75458, 46: 81494, 47: 88013, 48: 95054, 49: 102658, 50: 110870, 51: 119739, 52: 129318, 53: 139663, 54: 150836, 55: 162902, 56: 175934, 57: 190008, 58: 205208, 59: 221624, 60: 221624, 61: 221624, 62: 221624, 63: 221624, 64: 221624, 65: 238245, 66: 256113, 67: 275321, 68: 295970, 69: 318167, 70: 342029, 71: 367681, 72: 395257, 73: 424901, 74: 456768, 75: 488741, 76: 522952, 77: 559558, 78: 598727, 79: 640637, 80: 685481, 81: 733464, 82: 784806, 83: 839742, 84: 898523, 85: 961419, 86: 1028718, 87: 1100728, 88: 1177778, 89: 1260222, 90: 1342136, 91: 1429374, 92: 1522283, 93: 1621231, 94: 1726611, 95: 1838840, 96: 1958364, 97: 2085657, 98: 2221224, 99: 2365603, 100: 2365603, 101: 2365603, 102: 2365603, 103: 2365603, 104: 2365603, 105: 2519367, 106: 2683125, 107: 2857528, 108: 3043267, 109: 3241079, 110: 3451749, 111: 3676112, 112: 3915059, 113: 4169537, 114: 4440556, 115: 4729192, 116: 5036589, 117: 5363967, 118: 5712624, 119: 6083944, 120: 6479400, 121: 6900561, 122: 7349097, 123: 7826788, 124: 8335529, 125: 8877338, 126: 9454364, 127: 10068897, 128: 10723375, 129: 11420394, 130: 12162719, 131: 12953295, 132: 13795259, 133: 14691950, 134: 15646926, 135: 16663976, 136: 17747134, 137: 18900697, 138: 20129242, 139: 21437642, 140: 22777494, 141: 24201087, 142: 25713654, 143: 27320757, 144: 29028304, 145: 30842573, 146: 32770233, 147: 34818372, 148: 36994520, 149: 39306677, 150: 41763344, 151: 44373553, 152: 47146900, 153: 50093581, 154: 53224429, 155: 56550955, 156: 60085389, 157: 63840725, 158: 67830770, 159: 72070193, 160: 76574580, 161: 81360491, 162: 86445521, 163: 91848366, 164: 97588888, 165: 103688193, 166: 110168705, 167: 117054249, 168: 124370139, 169: 132143272, 170: 140402226, 171: 149177365, 172: 158500950, 173: 168407259, 174: 178932713, 175: 190116006, 176: 201998256, 177: 214623147, 178: 228037093, 179: 242289411, 180: 256826775, 181: 272236381, 182: 288570563, 183: 305884796, 184: 324237883, 185: 343692155, 186: 364313684, 187: 386172505, 188: 409342855, 189: 433903426, 190: 459937631, 191: 487533888, 192: 516785921, 193: 547793076, 194: 580660660, 195: 615500299, 196: 652430316, 197: 691576134, 198: 733070702, 199: 777054944, 200: 2207026470, 201: 2648431764, 202: 3178118116, 203: 3813741739, 204: 4576490086, 205: 5491788103, 206: 6590145723, 207: 7908174867, 208: 9489809840, 209: 11387771808, 210: 24142076232, 211: 25590600805, 212: 27126036853, 213: 28753599064, 214: 30478815007, 215: 32307543907, 216: 34245996541, 217: 36300756333, 218: 38478801712, 219: 40787529814, 220: 84838062013, 221: 88231584493, 222: 91760847872, 223: 95431281786, 224: 99248533057, 225: 103218474379, 226: 107347213354, 227: 111641101888, 228: 116106745963, 229: 120751015801, 230: 246332072234, 231: 251258713678, 232: 256283887951, 233: 261409565710, 234: 266637757024, 235: 271970512164, 236: 277409922407, 237: 282958120855, 238: 288617283272, 239: 294389628937, 240: 594667050452, 241: 600613720956, 242: 606619858165, 243: 612686056746, 244: 618812917313, 245: 625001046486, 246: 631251056950, 247: 637563567519, 248: 643939203194, 249: 650378595225, 250: 1}

    def __dir__(self):
        pass

    def __GetPercentage(self):
        return round(((Character.GetExp() / self.LevelToExp[Character.GetLevel()]) * 100), 2)

    def __GetWorld(self, LineEditID):
        if Terminal.GetComboBox('LoginServer') == 0:
            return
        elif Terminal.GetComboBox('LoginServer') == 1:
            IDToName = {0: 'Reboot',
                        1: 'GRAZED',
                        2: 'MYBCKN',
                        3: 'MYBCKN',
                        4: 'GRAZED',
                        5: 'GRAZED',
                        6: 'GRAZED',
                        7: 'GRAZED',
                        8: 'GRAZED',
                        9: 'MYBCKN',
                        10: 'MYBCKN',
                        11: 'MYBCKN',
                        12: 'MYBCKN',
                        13: 'Khroa',
                        14: 'Windia',
                        15: 'Khroa',
                        16: 'Bera',
                        17: 'Scania'}
            return IDToName[LineEditID]
        elif Terminal.GetComboBox('LoginServer') == 2:
            IDToName = {0: 'Luna',
                        1: 'EuReboot'}
            return IDToName[LineEditID]

    def __LogGM(self):
        try:
            worldStatus = ast.literal_eval(self.__ReadGMLogs())[self.__GetWorld(Terminal.GetComboBox('LoginWorld'))]
            worldsToCheck = ast.literal_eval(self.__ReadWorldsToLogOut())[self.__GetWorld(Terminal.GetComboBox('LoginWorld'))]
            if worldStatus == 'online' and bool(worldsToCheck):
                Terminal.SetCheckBox('Auto Login', False)
                Terminal.Logout()
            if worldStatus == 'offline' and bool(worldsToCheck):
                Terminal.SetCheckBox("Auto Login", True)
        except:
            pass


    def __LogClient(self):
        if GameState.IsInGame():
            is_logged = self.__Items()
            if not is_logged:
                print('TMRemote> Unable to log items: {}'.format(datetime.datetime.now()))
        else:
            is_logged = self.__Disconnect()
            if not is_logged:
                print('TMRemote> Unable to log disconnect: {}'.format(datetime.datetime.now()))

        self.__LogGM()


    def __Items(self):
        try:
            IGN = Character.GetName()
        except:
            IGN = 'N/A'
        Channel = GameState.GetChannel()
        World = GameState.GetWorldID()
        Level = Character.GetLevel()
        CharID = Character.GetID()
        PercentageExp = GetPercentage()
        VJSymbol = Inventory.GetItemCount(1712001)
        ChuSymbol = Inventory.GetItemCount(1712002)
        LachSymbol = Inventory.GetItemCount(1712003)
        ArcanaSymbol = Inventory.GetItemCount(1712004)
        MorrasSymbol = Inventory.GetItemCount(1712005)
        EsferaSymbol = Inventory.GetItemCount(1712006)
        StigmaAmount = Inventory.GetItemCount(4001868)
        CoreAmount = Inventory.GetItemCount(4001842)
        TradNodes = Inventory.GetItemCount(2435719)
        UntradNodes = Inventory.GetItemCount(2436324)
        MesoCount = Character.GetMeso()
        DropletCount = Inventory.GetItemCount(4001878)
        EsferaDropletCount = Inventory.GetItemCount(4001879)
        ProtAmount = Inventory.GetItemCount(2531000) + Inventory.GetItemCount(2531001) + \
            Inventory.GetItemCount(2531004) + Inventory.GetItemCount(2531005)
        CssAmount = Inventory.GetItemCount(2049004) + Inventory.GetItemCount(2049009) + Inventory.GetItemCount(2049011) + \
            Inventory.GetItemCount(2049018) + Inventory.GetItemCount(2049022)
        PotentialScrolls = Inventory.GetItemCount(2049401)

        items = {'IGN': IGN,
                 'World': World,
                 'CharID': CharID,
                 'Channel': Channel,
                 'Level': Level,
                 'EXP': PercentageExp,
                 'VJSymbols': VJSymbol,
                 'ChuChuSymbols': ChuSymbol,
                 'LacheleinSymbols': LachSymbol,
                 'ArcanaSymbols': ArcanaSymbol,
                 'MorrasSymbol': MorrasSymbol,
                 'EsferaSymbols': EsferaSymbol,
                 'StigmaCores': StigmaAmount,
                 'ACores': CoreAmount,
                 'TradableNodes': TradNodes,
                 'UntradableNodes': UntradNodes,
                 'Meso': MesoCount,
                 'Droplets': DropletCount,
                 'EsferaDroplets': EsferaDropletCount,
                 'ProtectionScrolls': ProtAmount,
                 'CleanSlate': CssAmount,
                 'PotentialScrolls': PotentialScrolls}

        try:
            self.__toFile('TMRemote/temp/logs', 'ab', items)
            return True
        except:
            try:
                with open('TMRemote/temp/logs', 'wb+')as temp:
                    pass
                self.__toFile('TMRemote/temp/logs', 'ab', items)
                return True
            except:
                return False

    def __Disconnect(self):
        currentTime = datetime.datetime.now()
        disconnect = {'disconnect': '{0}: {1}: {2} {3}/{4}/{5}'.format(currentTime.hour, currentTime.minute,
                                                                       currentTime.second, currentTime.day,
                                                                       currentTime.month, currentTime.year)}

        self.__toFile('TMRemote/temp/logs', 'ab', disconnect)
        return True

        try:
            with open('TMRemote/temp/logs', 'wb+')as temp:
                pass
            Log.toFile('TMRemote/temp/logs', 'ab', disconnect)
            return True
        except:
            return False

    def __ReadGMLogs(self):
        try:
            with open('TMRemote/temp/GMStatus', 'rb') as file:
                GMStatus = pickle.load(file)
            return GMStatus
        except FileNotFoundError:
            pass

    def __ReadWorldsToLogOut(self):
        try:
            with open('TMRemote/temp/WorldToCheck', 'rb') as file:
                WorldsToCheck = pickle.load(file)
            return GMStatus
        except FileNotFoundError:
            pass

    def __toFile(self, filename, mode, data):
        with open(filename, mode) as PickleFile:
            pickle.dump(data, PickleFile)

    def main(self):
        try:
            self.__LogClient()
        except:
            pass
