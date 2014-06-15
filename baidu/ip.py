"""百度ip地址定位api简单封装

详细请参考文档：http://developer.baidu.com/map/ip-location-api.htm
"""

import json
from urllib.parse import urlencode
from urllib.request import urlopen


class BaiduIp():
    url = 'http://api.map.baidu.com/location/ip?'

    def __init__(self, ak, ip='', coor='bd09ll'):
        self.ak = ak
        self.ip = ip
        self.coor = coor

    def get_url(self):
        data = {
            'ip': self.ip,
            'ak': self.ak,
            'coor': self.coor
        }
        return BaiduIp.url + urlencode(data)

    def get_by_ip(self, ip=''):
        self.ip = ip
        response = urlopen(self.get_url())
        result = json.loads(response.read().decode())
        return result


if __name__ == '__main__':
    p = BaiduIp('填入ak')
    print(p.get_by_ip())