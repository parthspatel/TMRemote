import ast
import os
import pickle, shelve

import requests
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from backend.auth import Auth, encryption
from backend.log import Log


class apiKeyThread(QThread):
    def __init__(self, username, password, setApiKey, getApiKey):
        QThread.__init__(self)
        self.getUsername = username
        self.getPassword = password

        self.setApiKey = setApiKey
        self.getApiKey = getApiKey

        self.sleep_time = 60
        self.sleep_time_const = self.sleep_time

    def __getApiKey(self):
        with shelve.open('TMRemote', 'c') as tmRemoteFile:
            try:
                token = encryption().decrypt(tmRemoteFile['apiKey'], 'OeUL5JePrvTZr7eXWdmytEvjkFa65Kn3YY2RaNUjO5Ur5q6fQPthoLhBLSv66yG9s5RW8R1xat57JKPOkSaaYyP9xMB1D0nivG7X6buAoEai3HPbOlaI75trv80JCB4ilmOIK7ZlldxMmzUFL2m0bTYXS8DXlInYa6F86tOWIJNZSHyfcBg9vxvhrVxVCslGlOVoPYjhWFn1C5t4EUGj2DkgNstRHmpig5J6bDS22Cz9DSyjDlj8kGLDyp5HiJgdCHgl93Tl4bH4vJKRAt7pI3f2R73DpkXn2a4XJPE7yv1B5q7jljRLhTLzf1cjataTeLAbEQlrLTApv3aeKsZC9Eyli7JkfhdOugiIPa2zPyhnXcDpkeRr4fu4SmQJ4Lew8VJ9qjO7mgzH1sLp3VOn90fc1TJ1y8PdiwtGblJGddTjnW4HWeowR0DfgdroOAOZ4OCa0yqkwL03uElBccVvgfxutJy7MwyTlykdLt3eoqrZpyGnt9tN')
                return token
            except KeyError:
                pass
        headers = {'User-Agent': 'TMR Bot'}
        try:
            data = {'username': self.getUsername(),
                    'password': self.getPassword()}
        except:
            return 'API Key Error: No username or password'
        try:
            token = ast.literal_eval(requests.post(
                'https://beta.tmremote.io/api/login', headers=headers, data=data).text)['token']
            with shelve.open('TMRemote','c') as tmRemoteFile:
                token = encryption().encrypt(token, 'OeUL5JePrvTZr7eXWdmytEvjkFa65Kn3YY2RaNUjO5Ur5q6fQPthoLhBLSv66yG9s5RW8R1xat57JKPOkSaaYyP9xMB1D0nivG7X6buAoEai3HPbOlaI75trv80JCB4ilmOIK7ZlldxMmzUFL2m0bTYXS8DXlInYa6F86tOWIJNZSHyfcBg9vxvhrVxVCslGlOVoPYjhWFn1C5t4EUGj2DkgNstRHmpig5J6bDS22Cz9DSyjDlj8kGLDyp5HiJgdCHgl93Tl4bH4vJKRAt7pI3f2R73DpkXn2a4XJPE7yv1B5q7jljRLhTLzf1cjataTeLAbEQlrLTApv3aeKsZC9Eyli7JkfhdOugiIPa2zPyhnXcDpkeRr4fu4SmQJ4Lew8VJ9qjO7mgzH1sLp3VOn90fc1TJ1y8PdiwtGblJGddTjnW4HWeowR0DfgdroOAOZ4OCa0yqkwL03uElBccVvgfxutJy7MwyTlykdLt3eoqrZpyGnt9tN')
                tmRemoteFile['apiKey'] = token
            return token
        except Exception as ex:
            return f'API Key Error: Token request failed with {ex}'

    def run(self):
        num_failed = 0
        apiKey  = self.__getApiKey()
        while True:

            if 'failed' in apiKey:
                self.sleep_time = 600 #10mins
                num_failed += 1
                if 5 < num_failed:
                    break
                apiKey  = self.__getApiKey()
            else:
                self.sleep_time = 3600
                self.setApiKey(apiKey)
            self.sleep(self.sleep_time)
