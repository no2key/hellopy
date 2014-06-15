"""tornado 上应用 reCaptcha 示例
[reCaptcha](http://zh.wikipedia.org/wiki/ReCAPTCHA)
[reCaptcha Doc](https://developers.google.com/recaptcha/intro)

吐槽：reCaptcha难度实在太高，智商捉急
"""


from urllib.request import urlopen
from urllib.parse import urlencode
import tornado.httpserver
import tornado.ioloop
import tornado.web


#获取key: https://www.google.com/recaptcha/whyrecaptcha
publickey = '输入你的 public key'
privatekey = '输入你的 private key'


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', IndexHandler)
        ]
        settings = dict(
            template_path="templates",
        )

        tornado.web.Application.__init__(self, handlers, **settings)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html', publickey=publickey)

    def post(self):
        url = 'http://www.google.com/recaptcha/api/verify'

        #验证码
        challenge = self.get_argument('recaptcha_challenge_field')
        #用户输入
        response = self.get_argument('recaptcha_response_field')

        data = {
            'privatekey': privatekey,
            'remoteip': self.request.remote_ip,
            'challenge': challenge,
            'response': response
        }

        res = urlopen(url, data=urlencode(data).encode())
        #获取验证结果，这里直接将返回结果输出到页面
        self.write(res.read().decode())


if __name__ == '__main__':
    server = tornado.httpserver.HTTPServer(Application())
    server.listen(10001)
    tornado.ioloop.IOLoop.instance().start()