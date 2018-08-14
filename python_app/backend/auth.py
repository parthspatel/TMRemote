import datetime

import requests


class Auth():
    def authenticate(func):
        def authenticate_and_call(*args, **kwargs):
            def auth_ban_detection():
                data = {'key': args[0].getApiKey(),
                        'name': args[0].getUsername()}
                return requests.post(args[0].links['banDetection'],
                                     data=data).text
            token = auth_ban_detection()
            if 'error' in token:
                now = datetime.datetime.now().isoformat(' ', 'seconds')
                args[0].logs.post(now, 'Authentication Failed')
                args[0].sleep_time = 10
                return

            return func(token=token,
                        *args, **kwargs)
        return authenticate_and_call
