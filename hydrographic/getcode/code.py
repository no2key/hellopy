"""获取code编码
包括各省和山东省各市的编码及输油管线类型和运营主体编码
"""


from urllib.request import urlopen, Request, HTTPError
import json


class Post():

    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def post(self):
        for key in self.url.keys():
            r = Request(self.url[key], headers=self.headers)
            try:
                p = urlopen(r)
                p = p.read().decode()
                d = json.JSONDecoder()
                p = d.decode(p)
                print("<<<<<{}>>>>> start".format(key))
                print("核查地址：{}".format(self.url[key]))
                for t in p:
                    print('{}:{}:{}'.format(t['rowId'], t['fullName'], t['identificationCode']))

                print("<<<<{}>>>>> end".format(key))
                print("--------------------------------------")
                #print(p)
                #print((p.getcode()))
            except HTTPError as err:
                print(err)

urls = dict()

urls['运营主体'] = 'http://114.251.10.55/GWISWeb/tbBusGasStationList/queryCodTable/10000020'
urls['输油管线类型'] = 'http://114.251.10.55/GWISWeb/tbBusGasStationList/queryCodTable/10000021'
urls['省份名称'] = 'http://114.251.10.55/GWISWeb/tbBusGasStationList/queryCascade/10000003/1'
urls['地市名称'] = 'http://114.251.10.55/GWISWeb/tbBusGasStationList/queryCascade/10000003/370000'
urls['济南'] = 'http://114.251.10.55/GWISWeb/tbBusGasStationList/queryCascade/10000003/370100'
urls['青岛'] = 'http://114.251.10.55/GWISWeb/tbBusGasStationList/queryCascade/10000003/370200'
urls['淄博市'] = 'http://114.251.10.55/GWISWeb/tbBusGasStationList/queryCascade/10000003/370300'
urls['枣庄市'] = 'http://114.251.10.55/GWISWeb/tbBusGasStationList/queryCascade/10000003/370400'
urls['东营市'] = 'http://114.251.10.55/GWISWeb/tbBusGasStationList/queryCascade/10000003/370500'
urls['烟台市'] = 'http://114.251.10.55/GWISWeb/tbBusGasStationList/queryCascade/10000003/370600'
urls['潍坊市'] = 'http://114.251.10.55/GWISWeb/tbBusGasStationList/queryCascade/10000003/370700'
urls['济宁市'] = 'http://114.251.10.55/GWISWeb/tbBusGasStationList/queryCascade/10000003/370800'
urls['泰安'] = 'http://114.251.10.55/GWISWeb/tbBusGasStationList/queryCascade/10000003/370900'
urls['威海市'] = 'http://114.251.10.55/GWISWeb/tbBusGasStationList/queryCascade/10000003/371000'
urls['日照市'] = 'http://114.251.10.55/GWISWeb/tbBusGasStationList/queryCascade/10000003/371100'
urls['莱芜市'] = 'http://114.251.10.55/GWISWeb/tbBusGasStationList/queryCascade/10000003/371200'
urls['临沂市'] = 'http://114.251.10.55/GWISWeb/tbBusGasStationList/queryCascade/10000003/371300'
urls['德州市'] = 'http://114.251.10.55/GWISWeb/tbBusGasStationList/queryCascade/10000003/371400'
urls['聊城市'] = 'http://114.251.10.55/GWISWeb/tbBusGasStationList/queryCascade/10000003/371500'
urls['滨州市'] = 'http://114.251.10.55/GWISWeb/tbBusGasStationList/queryCascade/10000003/371600'
urls['菏泽'] = 'http://114.251.10.55/GWISWeb/tbBusGasStationList/queryCascade/10000003/371700'


header = {
    'Cookie': '',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'
}

if __name__ == '__main__':
    po = Post(urls, header)
    po.post()