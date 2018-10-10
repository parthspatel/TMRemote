import re
import os.path
import urllib.request
import urllib.error
import base64
import gzip
import zlib
from io import BytesIO

# urls = 'https://www.gamekiller.net/threads/da-8-15-5m-range-trusted-vouched.3258642'


class GKRequest():
    def make_request(self, url, msg='bump'):
        response = [None]
        responseText = None

        if(self.request_www_gamekiller_net(url, response, msg)):
            response[0].close()
            return True
        return False

    def read_response(self, response):
        if response.info().get('Content-Encoding') == 'gzip':
            buf = BytesIO(response.read())
            return gzip.GzipFile(fileobj=buf).read().decode('utf8')

        elif response.info().get('Content-Encoding') == 'deflate':
            decompress = zlib.decompressobj(-zlib.MAX_WBITS)
            inflated = decompress.decompress(response.read())
            inflated += decompress.flush()
            return inflated.decode('utf8')

        return response.read().decode('utf8')

    def request_www_gamekiller_net(self, url, response, msg):
        response[0] = None

        try:
            req = urllib.request.Request(
                url + "/add-reply")

            req.add_header("Connection", "keep-alive")
            req.add_header("Accept", "application/json, text/javascript, */*; q=0.01")
            req.add_header(
                "X-Ajax-Referer", url + "/#post-3267997")
            req.add_header("X-Requested-With", "XMLHttpRequest")
            req.add_header(
                "User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36")
            req.add_header("Origin", "https://www.gamekiller.net")
            req.add_header("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8")
            req.add_header("DNT", "1")
            req.add_header(
                "Referer", url + "/")
            req.add_header("Accept-Encoding", "gzip, deflate, br")
            req.add_header("Accept-Language", "en-US,en;q=0.9")
            req.add_header("Cookie", "__cfduid=daed5dcf0d374e0f44e38919cd4bd89a51526281857; xf_session=2658f3a62dd00fee3029c76e147cd6a2; xf_user=1028033%2C7c7c0b7de39077938308b57ce5913194a2556261")

            thread = url[url.rfind('/')+1:]
            msg = msg.replace(' ', '+')
            body = b"message_html=%3Cp%3E" + msg.encode() + b"%3C%2Fp%3E&_xfRelativeResolver=https%3A%2F%2Fwww.gamekiller.net%2Fthreads%2F" + thread.encode() + \
                b"%2F&attachment_hash=d873e1b659fdc4986f7ce5bb0f4b018c&last_date=1526992332&last_known_date=1526992332&_xfToken=881308%2C1527021349%2Cbb153a8252cf6002ce01ac1c68157fd9e084bd64&_xfRequestUri=%2Fthreads%2F" + \
                thread.encode() + b"%2F&_xfNoRedirect=1&_xfToken=881308%2C1527021349%2Cbb153a8252cf6002ce01ac1c68157fd9e084bd64&_xfResponseType=json"

            response[0] = urllib.request.urlopen(req, body)

        except urllib.error.URLError as e:
            if not hasattr(e, "code"):
                return False
            response[0] = e
        except:
            return False
        return True


if __name__ == '__main__':
    bSucc = GKRequest().make_request('https://www.gamekiller.net/threads/da-8-15-5m-range-trusted-vouched.3258642')
