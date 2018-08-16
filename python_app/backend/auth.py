import socket

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
        level_dict = {'basic': 'botLogs',
                      'prime': 'banDetection'}

        def authenticate_and_call(*args, **kwargs):
            def auth_ban_detection():
                try:
                    data = {'key': args[0].getApiKey(),
                            'name': args[0].getUsername()}
                    status = requests.post(args[0].links[level_dict[level]],
                                           data=data).text
                    return status
                except Exception as ex:
                    raise ex
            try:
                token = auth_ban_detection()
            except Exception as ex:
                return f'No Internet: {ex}'
            else:
                if 'error' in token:
                    args[0].sleep_time = 10
                    return f'Authentication Failed: {token}'
                args[0].sleep_time = args[0].sleep_time_const
                return func(token=token,
                            *args, **kwargs)
        return authenticate_and_call
