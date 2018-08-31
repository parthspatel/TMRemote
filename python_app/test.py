import ast
import pprint as pp

import requests

headers = {'User-Agent': 'TMR Bot'}
dataSet = {'username': 'Mehodin',
           'password': 'Edocsgnageot09'}

token = ast.literal_eval(requests.post(
    'https://beta.tmremote.io/api/login', headers=headers, data=dataSet).text)['token']

print(type(requests.post(
    'https://beta.tmremote.io/api/login', headers=headers, data=dataSet)))

print(requests.post(
    'https://beta.tmremote.io/api/login', headers=headers, data=dataSet).text.status_code)

headers = {'User-Agent': 'TMR Bot',
           'Authorization': 'Bearer {}'.format(token)}

# print(headers)

gm_det = requests.get(
    'https://beta.tmremote.io/api/gm/status', headers=headers).text

# pp.pprint(gm_det)
