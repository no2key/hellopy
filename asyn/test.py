"""tornado异步测试
server.py 模拟外部资源提供服务器

"""

import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.gen
from tornado.httpclient import AsyncHTTPClient, HTTPClient


class IndexHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        url = 'http://localhost:10002'

        #同步
        # client = HTTPClient()
        # response = client.fetch(url)

        #异步
        client = AsyncHTTPClient()
        response = yield tornado.gen.Task(client.fetch, url)

        self.write(response.body.decode())
        self.finish()


class TestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('test is ok')

if __name__ == '__main__':
    app = tornado.web.Application(
        handlers=[
            (r'/', IndexHandler),
            (r'/test', TestHandler),
        ]
    )

    tornado.httpserver.HTTPServer(app).listen(10001)
    tornado.ioloop.IOLoop.instance().start()
