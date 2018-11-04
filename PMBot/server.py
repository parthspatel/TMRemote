import requests

class Server(object):
    def __init__(self, token, discord="https://discordapp.com/api/v6/"):
        self.discord = discord
        self.token = token

    def join_server(self, invite, proxy):
        return requests.post(self.discord + "invite/" + invite, proxies=proxy, headers={"Authorization": self.token})
