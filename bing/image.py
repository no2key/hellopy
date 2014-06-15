"""获取每日bing背景图
    api: http://cn.bing.com/HPImageArchive.aspx?format=xml&idx=0&n=1
"""
from xml.etree import ElementTree
from urllib.request import urlopen
from urllib.parse import urlencode
import json


class BingImage():
    #api接口地址
    url = 'http://cn.bing.com/HPImageArchive.aspx?'

    def __init__(self, idx=0, n=1):
        self.idx = idx
        self.n = n
        self.data = self.get_data()

    def get_image(self):
        """获取 image
        """
        return 'http://s.cn.bing.net' + self.data['url']

    def get_date(self):
        """image 日期
        """
        return self.data['enddate']

    def get_copyright(self):
        """image 描述
        """
        return self.data['copyright']

    def get_copyright_link(self):
        """image 搜索连接
        """
        return self.data['copyrightlink']

    def get_json_format(self):
        """返回json格式数据
        """
        data = {
            'image': self.get_image(),
            'date': self.get_date(),
            'copyright': self.get_copyright(),
            'copyrightlink': self.get_copyright_link(),
        }
        return json.dumps(data)

    def get_data(self):
        re = self._fetch()
        root = ElementTree.fromstring(re)
        return {child.tag: child.text for child in root[0]}

    def _fetch(self):
        response = urlopen(self._get_url())
        return response.read().decode()

    def _get_url(self):
        data = {
            'format': 'xml',
            'idx': self.idx,
            'n': self.n,
        }
        return self.url + urlencode(data)

if __name__ == '__main__':
    bing = BingImage(0, 1)
    print(bing.get_image())
    print(bing.get_copyright())
    print(bing.get_copyright_link())
    print(bing.get_date())
    print(bing.get_json_format())