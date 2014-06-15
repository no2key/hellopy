import time
import tornado.ioloop
import tornado.httpserver
import tornado.web
from tornado import httpclient
from tornado import gen


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexHandler),
            (r"/now", BitNowHandler),
            (r"/chartapi", ChartApiHandler),
            (r"/chart", ChartHandler),
        ]
        settings = dict(
            template_path="templates",
            static_path="static",
        )
        tornado.web.Application.__init__(self, handlers, **settings)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')


class ChartHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('chart.html')


class BitNowHandler(tornado.web.RequestHandler):
    count = 0
    last_time = int(time.time())
    data = ''

    @tornado.gen.coroutine
    def get(self):
        """每隔5秒重新获取一次数据"""
        now_time = int(time.time())
        if now_time - BitNowHandler.last_time >= 5:
            BitNowHandler.last_time = now_time
            BitNowHandler.count += 1
            print(BitNowHandler.count)
            client = httpclient.AsyncHTTPClient()
            url = 'http://blockchain.info/ticker'
            response = yield gen.Task(client.fetch, url)
            BitNowHandler.data = response.body.decode()
        print(str(BitNowHandler.data))
        self.write(str(BitNowHandler.data))
        self.finish()


class ChartApiHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        url = 'http://blockchain.info/charts/market-price?format=json'
        client = httpclient.AsyncHTTPClient()
        response = yield gen.Task(client.fetch, url)
        data = response.body.decode()
        self.write(data)
        self.finish()


if __name__ == "__main__":
    server = tornado.httpserver.HTTPServer(Application())
    server.listen(8088)
    tornado.ioloop.IOLoop.instance().start()