import requests
import urllib

class sendReply():
    def __init__(self, url, message):
        self.url = url
        self.message = message
        self.body = None
        self.thread = self.url[self.url.rfind('/')+1:]
        print(self.thread)
        self.req = urllib.request.Request(
            url + "/add-reply")
        
        self.__encodeHeaders()
        self.__sendRequest()

    def __encodeHeaders(self):
        self.req.add_header("Connection", "keep-alive")
        self.req.add_header("Accept", "application/json, text/javascript, */*; q=0.01")
        self.req.add_header("X-Ajax-Referer", self.url + "/#post-3267997")
        self.req.add_header("X-Requested-With", "XMLHttpRequest")
        self.req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36")
        self.req.add_header("Origin", "https://www.gamekiller.net")
        self.req.add_header("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8")
        self.req.add_header("DNT", "1")
        self.req.add_header("Referer", self.url + "/")
        self.req.add_header("Accept-Encoding", "gzip, deflate, br")
        self.req.add_header("Accept-Language", "en-US,en;q=0.9")
        self.req.add_header("Cookie", "__cfduid=daed5dcf0d374e0f44e38919cd4bd89a51526281857; xf_session=2658f3a62dd00fee3029c76e147cd6a2; xf_user=1028033%2C7c7c0b7de39077938308b57ce5913194a2556261")

    def __sendRequest(self):
        self.body = b"message_html=%3Cp%3E" + self.message.encode() + b"%3Cbr%3E%3C%2Fp%3E&_xfRelativeResolver=https%3A%2F%2Fwww.gamekiller.net%2Fthreads%2F"+self.thread.encode()+b"2F&attachment_hash=f4e23a6aabda164ddd3de765026cc318&last_date=1539019477&last_known_date=1539019477&_xfToken=1028033%2C1539166234%2Ccaf64a93153733319886138e85b7bfd3e393cf2f&_xfRequestUri=%2Fthreads%2F" + self.thread.encode() + b"%2F&_xfNoRedirect=1&_xfToken=1028033%2C1539166234%2Ccaf64a93153733319886138e85b7bfd3e393cf2f&_xfResponseType=json"
        response = urllib.request.urlopen(self.req, self.body)


sendReply(url = 'https://www.gamekiller.net/threads/oh-do-you-guys-remember.3270011', message = 'justTesting')