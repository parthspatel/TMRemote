from base64 import b64encode
from binascii import hexlify
from hashlib import sha512
from http import client
from http import HTTPStatus
import json
from time import sleep
from datetime import datetime, timezone, timedelta
import sys

# User-Agent
NXL_USER_AGENT = 'NexonLauncher.nxl-18.11.01-372-365f004'

# nexon client


class nexon_client:

    def __init__(self, email, password, device_id):
        self.email = email
        self.password = password
        self.device_id = device_id
        self.id_token = ""
        self.access_token = ""
        self.id_token_expiry_time = datetime.now()
        self.access_token_expiry_time = datetime.now()

    def login(self):
        connection = client.HTTPSConnection('www.nexon.com', 443)
        headers = {
            'Accept-Encoding': 'identity',
            'Connection': 'close',
            'User-Agent': NXL_USER_AGENT,
            'Content-Type': 'application/json'
        }
        body = {
            'id': self.email,
            'password': hexlify(sha512(bytes(self.password, 'utf-8')).digest()).decode('utf-8'),
            'auto_login': False,
            'client_id': '7853644408',
            'scope': 'us.launcher.all',
            'device_id': self.device_id
        }
        connection.request('POST', '/account-webapi/login/launcher', json.dumps(body), headers)
        response = connection.getresponse()
        if response.status != HTTPStatus.OK:
            # fail
            return False

        response_body = json.loads(response.read().decode('utf-8'))
        self.id_token = response_body['id_token']
        self.access_token = response_body['access_token']
        self.id_token_expiry_time = datetime.now() + timedelta(0, response_body['id_token_expires_in'])
        self.access_token_expiry_time = datetime.now() + timedelta(0, response_body['access_token_expires_in'])
        return True

    def logout(self):
        connection = client.HTTPSConnection('www.nexon.com', 443)
        headers = {
            'Accept-Encoding': 'identity',
            'Connection': 'close',
            'User-Agent': NXL_USER_AGENT,
            'Content-Type': 'application/json'
        }
        body = {
            'device_id': self.device_id,
            'id_token': self.id_token,
            'access_token': self.access_token,
            'auto_login': None,
        }
        connection.request('POST', '/account-webapi/logout/launcher', json.dumps(body), headers)
        response = connection.getresponse()
        if response.status != HTTPStatus.OK:
            # fail
            return False
        return True

    def refresh(self):
        connection = client.HTTPSConnection('www.nexon.com', 443)
        headers = {
            'Accept-Encoding': 'identity',
            'Authorization': 'bearer ' + b64encode(bytes(self.access_token, 'utf-8')).decode('utf-8'),
            'Cookie': 'nxtk=' + self.access_token + ';domain=.nexon.net;path=/;',
            'Connection': 'close',
            'Content-Type': 'application/json',
            'User-Agent': NXL_USER_AGENT,
        }
        body = {
            'device_id': self.device_id,
            'client_id': '7853644408',
            'id_token': self.id_token
        }
        connection.request('POST', '/account-webapi/login/launcher/refresh', json.dumps(body), headers)
        response = connection.getresponse()
        if response.status != HTTPStatus.OK:
            # fail
            return False

        response_body = json.loads(response.read().decode('utf-8'))
        self.id_token = response_body['id_token']
        self.access_token = response_body['access_token']
        self.id_token_expiry_time = datetime.now() + timedelta(0, response_body['id_token_expires_in'])
        self.access_token_expiry_time = datetime.now() + timedelta(0, response_body['access_token_expires_in'])
        return True

    def products(self):
        connection = client.HTTPSConnection('api.nexon.io', 443)
        headers = {
            'Accept-Encoding': 'identity',
            'User-Agent': NXL_USER_AGENT,
            'Content-Type': 'application/json',
            'Authorization': 'bearer ' + b64encode(bytes(self.access_token, 'utf-8')).decode('utf-8'),
            'Cookie': 'nxtk=' + self.access_token + ';domain=.nexon.net;path=/;',
            'Connection': 'close'
        }
        connection.request('GET', '/products/10100', None, headers)
        response = connection.getresponse()
        return response

    def check_playable(self, product_id):
        connection = client.HTTPSConnection('api.nexon.io', 443)
        headers = {
            'Accept-Encoding': 'identity',
            'User-Agent': NXL_USER_AGENT,
            'Content-Type': 'application/json',
            'Authorization': 'bearer ' + b64encode(bytes(self.access_token, 'utf-8')).decode('utf-8'),
            'Cookie': 'nxtk=' + self.access_token + ';domain=.nexon.net;path=/;',
            'Connection': 'close'
        }
        body = {
            'id_token': self.id_token,
            'device_id': self.device_id,
            'product_id': product_id
        }
        connection.request('POST', '/game-auth/v2/check-playable', json.dumps(body), headers)
        response = connection.getresponse()
        return response

    def passport():
        connection = client.HTTPSConnection('api.nexon.io', 443)
        headers = {
            'Accept-Encoding': 'identity',
            'User-Agent': NXL_USER_AGENT,
            'Content-Type': 'application/json',
            'Authorization': 'bearer ' + b64encode(bytes(self.access_token, 'utf-8')).decode('utf-8'),
            'Cookie': 'nxtk=' + self.access_token + ';domain=.nexon.net;path=/;',
            'Connection': 'close'
        }
        connection.request('GET', '/users/me/passport', None, headers)
        response = connection.getresponse()
        return response

# main


def check_playable(nclient, productid):
    response = nclient.check_playable(productid)
    if response.status != HTTPStatus.OK:
        response_body = json.loads(response.read().decode('utf-8'))

        error = response_body.get('error')
        if error is not None:
            code = error.get('code')
            if code == 801:
                # maintenance
                return True
    else:
        # not maintenance
        return False


def main():
    # login
    nclient = nexon_client("MehoGK@gmail.com", "a123456789", "e902372f6a92b7b9ad5f557851cbc711b190c22f04ac8a6d8c3f26e69bae8230")
    if nclient.login() is True:
        # products
        response = nclient.products()
        response_body = json.loads(response.read().decode('utf-8'))
        product_details = response_body.get('product_details')
        if product_details is not None:
            manifestUrl = product_details.get('manifestUrl')

        # refresh
        if nclient.refresh():
            pass

        # authorize
        maintenance = check_playable(nclient, '10100')
        return maintenance
        # logout
        nclient.logout()
