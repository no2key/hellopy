"""模拟外部资源服务器

"""

import time
import tornado.web
import tornado.httpserver
import tornado.ioloop


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        data = {
            'name': 'jim',
            'age': 20,
        }
        #模拟阻塞
        time.sleep(10)
        self.write(data)


if __name__ == '__main__':
    app = tornado.web.Application(
        handlers=[
            (r'/', IndexHandler)
        ]
    )

    tornado.httpserver.HTTPServer(app).listen(10002)
    tornado.ioloop.IOLoop.instance().start()

