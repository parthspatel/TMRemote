import hashlib
import socket
import subprocess

import requests


class Auth():
    def connected(func):
        def is_network_connection(host="1.1.1.1", port=53, timeout=3, *args, **kwargs):
            try:
                socket.setdefaulttimeout(timeout)
                socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(
                    (host, port))
                return func(*args, **kwargs)
            except Exception as ex:
                raise ex

        return is_network_connection

    def parametrized(dec):
        def layer(*args, **kwargs):
            def repl(f):
                return dec(f, *args, **kwargs)
            return repl
        return layer

    @parametrized
    def authenticate(func, level='basic'):
        level_dict = {'basic': 'logIn',
                      'prime': 'banDetection'}

        def authenticate_and_call(*args, **kwargs):
            print('inside authenticate_and_call func')

            def auth_ban_detection():
                print('inside auth_ban_detection func')
                try:
                    headers = {'User-Agent': 'TMR Bot'}
                    if level == 'prime':
                        apiKey = args[0].apiKey()
                        if 'error' in apiKey.lower():
                            return f'Authentication Failed API Key Error: {apiKey}'
                        headers.update(
                            {'Authorization': 'Bearer {}'.format(apiKey)})
                    else:
                        data = {'username': args[0].getUsername(),
                                'password': args[0].getPassword()}

                    link = args[0].links[level_dict[level]]
                    if 'http' in link.lower():
                        if level == 'prime':
                            status = requests.get(link, headers=headers)
                        else:
                            status = requests.post(
                                link, headers=headers, data=data)
                        statusCode = status.status_code
                        status = status.text
                    if statusCode == 401:
                        args[0].sleep_time = 10
                        return f'{level.capitalize()} Authentication Failed: {statusCode}'
                    elif statusCode != 200:
                        return f'{level.capitalize()} Authentication Failed: Something went wrong, status code: {statusCode}'
                    return func(token=status, *args, **kwargs)
                except Exception as ex:
                    return f'Auth Failed: {ex}'

            return auth_ban_detection()
        return authenticate_and_call

    class HardwareID():
        def __init__(self):
            self.HWIDCommand = 'WMIC csproduct get uuid'
            self.CpuCommand = 'WMIC cpu get ProcessorId'
            self.GpuCommand = 'WMIC path win32_VideoController get VideoMemoryType'
            self.GpuCommand2 = 'WMIC path win32_VideoController get AdapterRAM'
            self.shell = True
            self.hashed = None

        def __getBaseID(self):
            BaseID = subprocess.check_output(
                self.HWIDCommand, shell=self.shell)
            BaseID = ''.join(BaseID.decode('utf-8').split('\n')[-3].split('-'))
            return BaseID

        def __getCpuID(self):
            CpuID = subprocess.check_output(
                self.CpuCommand, shell=self.shell)
            CpuID = CpuID.decode('utf-8').split('\n')[1]
            return CpuID

        def __getGpuID(self):
            GpuID = subprocess.check_output(
                self.GpuCommand, shell=self.shell)
            GpuID = int(GpuID.decode('utf-8').split('\n')[1])
            return str(GpuID)

        def __getGpuID2(self):
            GpuID2 = subprocess.check_output(
                self.GpuCommand2, shell=self.shell)
            return GpuID2.decode().replace('\n', '')

        def __hash(self, id):
            return hashlib.sha256(id.encode('utf-8')).hexdigest()

        def __shift(self, id):
            l = list(id)
            return ''.join(l[-1:] + l[:-1])

        def __encrypt(self, id):
            return self.__shift(self.__hash(self.__shift(id)))

        def asStr(self):
            self.trueHWID = self.__getGpuID() + self.__getCpuID() + \
                self.__getGpuID2() + self.__getBaseID()
            self.trueHWID = self.trueHWID.replace(' ', '').replace('\r', '')
            return self.__encrypt(self.trueHWID)
