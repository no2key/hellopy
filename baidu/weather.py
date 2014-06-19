"""百度天气api
"""
import json
from urllib.parse import urlencode
from urllib.request import urlopen


class Weather():
    """百度天气查询api接口

    """
    #api接口地址
    API_URL = 'http://api.map.baidu.com/telematics/v3/weather?'

    def __init__(self, ak, output='json'):
        self.ak = ak
        self.output = output

    def get_weather(self, location='济南'):
        """获取城市天气
        """
        data = {
            'location': location,
            'output': self.output,
            'ak': self.ak,
        }

        url = Weather.API_URL + urlencode(data)
        response = urlopen(url)
        return json.loads(response.read().decode())


if __name__ == '__main__':
    w = Weather('873a531cec3212a4906a683572b248b5')
    print(w.get_weather('北京'))

