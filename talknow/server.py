from datetime import datetime
import os
import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')


class TalkHandler(tornado.websocket.WebSocketHandler):
    #记录连接的客户端
    clients = []

    def open(self):
        TalkHandler.clients.append(self)
        TalkHandler.send_to_all(str(id(self)) + ' 加入聊天')
        self.write_message('已与服务器建立连接')

    def on_message(self, message):
        TalkHandler.send_to_all(message)

    def on_close(self):
        TalkHandler.clients.remove(self)
        TalkHandler.send_to_all(str(id(self)) + '退出聊天')

    @staticmethod
    def send_to_all(message):
        """广播消息
        """
        #向每一个连接的客户端广播消息
        for c in TalkHandler.clients:
            c.write_message(datetime.now().strftime('time:%H:%M:%S:') + message)
            print(message)


setting = {
    'template_path': os.path.join(os.path.dirname(__file__), 'template'),
    'static_path': os.path.join(os.path.dirname(__file__), 'static'),
}

app = tornado.web.Application(
    handlers=[
        (r"/", IndexHandler),
        (r"/talk", TalkHandler),
    ],
    **setting
)


if __name__ == '__main__':
    tornado.httpserver.HTTPServer(app).listen(8000)
    tornado.ioloop.IOLoop.instance().start()