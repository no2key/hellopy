"""oauth 获取token

"""

import json
import os.path
from urllib.request import urlopen
from urllib.parse import urlencode
import tornado.web
import tornado.httpserver
import tornado.ioloop

#API Key
client_id = '需要填写'
#Secret Key
client_secret = '需要填写'


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('ok')


class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        url = 'https://openapi.baidu.com/oauth/2.0/authorize?'
        data = {
            'client_id': client_id,
            'response_type': 'code',
            #回调地址
            'redirect_uri': 'http://www.maguowei.com/auth',
        }
        url = url + urlencode(data)
        self.render('login.html', url=url)


class AuthHandler(tornado.web.RequestHandler):
    def get(self):
        code = self.get_argument('code', '')
        if code:
            #获取access_token
            token_url = 'https://openapi.baidu.com/oauth/2.0/token?'
            data = {
                'grant_type': 'authorization_code',
                'code': code,
                'client_id': client_id,
                'client_secret': client_secret,
                'redirect_uri': 'http://www.maguowei.com/auth',
            }

            response = urlopen(token_url, urlencode(data).encode())
            j = json.loads(response.read().decode())
            #获取当前用户信息
            url = 'https://openapi.baidu.com/rest/2.0/passport/users/getLoggedInUser?'
            data = {
                'access_token': j['access_token']
            }
            url += urlencode(data)
            r = urlopen(url)
            self.write(r.read())


if __name__ == '__main__':
    app = tornado.web.Application(
        handlers=[
            (r'/', IndexHandler),
            (r'/login', LoginHandler),
            (r'/auth', AuthHandler),
        ],
        static_path=os.path.join(os.path.dirname(__file__), 'static'),
        template_path=os.path.join(os.path.dirname(__file__), 'template'),
    )

    tornado.httpserver.HTTPServer(app).listen(80)
    tornado.ioloop.IOLoop.instance().start()