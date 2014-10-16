import requests


class Zhuanlan():
    url = 'http://zhuanlan.zhihu.com/shoucang/19859546'

    def __init__(self):
        pass

    def get_html(self):
        return requests.get(self.url).text

if __name__ == '__main__':
    zhuanlan = Zhuanlan()
    print(zhuanlan.get_html())
