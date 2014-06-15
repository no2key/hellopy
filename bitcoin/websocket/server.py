import tornado.ioloop
import tornado.httpserver
import tornado.web
import tornado.websocket
import tornado.gen
from tornado import httpclient


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexHandler),
            (r"/now", BitNowHandler),
        ]
        settings = dict(
            template_path="templates",
            static_path="static",
        )
        tornado.web.Application.__init__(self, handlers, **settings)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')


class BitNowHandler(tornado.websocket.WebSocketHandler):
    clients = []
    data = dict()

    def open(self):
        print(str(id(self)) + '建立连接')
        BitNowHandler.clients.append(self)

    @tornado.gen.engine
    @tornado.web.asynchronous
    def on_message(self, message):
        client = httpclient.AsyncHTTPClient()
        response = yield tornado.gen.Task(client.fetch, 'http://blockchain.info/ticker')
        BitNowHandler.data = response.body.decode()
        BitNowHandler.send_to_all(BitNowHandler.data)

    @staticmethod
    def send_to_all(message):
        for c in BitNowHandler.clients:
            c.write_message(message)

    def on_close(self):
        print(str(id(self)) + '退出连接')
        BitNowHandler.clients.remove(self)


if __name__ == "__main__":
    server = tornado.httpserver.HTTPServer(Application())
    server.listen(9999)
    tornado.ioloop.IOLoop.instance().start()