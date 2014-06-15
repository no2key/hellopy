"""数据上传主类
"""


from urllib.request import urlopen, Request, HTTPError
import urllib.parse


class Post():
    """数据上传

    """
    #统计计数
    number = 0
    error_number = 0
    #post数据
    data = {}

    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def post(self, data):
        data = urllib.parse.urlencode(data)
        data = data.encode()
        r = Request(self.url, headers=self.headers)
        try:
            p = urlopen(r, data=data)
            #print(p.read().decode())
            #print((p.getcode()))
            p.close()
            print('第{}条记录上传成功'.format(self.number+1))

        except HTTPError as err:
            print('第{}条记录发生错误:{}'.format(self.number+1, err))
            self.error_number += 1

    def start(self):
        print("<<< 开始上传数据 >>>")
        with open('data.txt', 'rb') as f:
            for line in f:
                line = line.decode().strip().split(',')
                print(line)
                self.data['projectName'], self.data['projectCode'], self.data['provinceCode'], self.data['cityCode'],\
                    self.data['countyCode'], self.data['orderCode'], self.data['hydrologicalCodeOfLevel1'],\
                    self.data['hydrologicalCodeOfLevel2'], self.data['longitudeDegree'],\
                    self.data['longitudeMinute'], self.data['longitudeSecond'], self.data['latitudedegree'],\
                    self.data['latitudeMinute1'], self.data['latitudesecond2'], self.data['isSurvey'],\
                    self.data['buildDate'], self.data['operatingSubjectId'], self.data['isBusiness'],\
                    self.data['totalOilTand'], self.data['doubleCansNumber'], self.data['isSeepageControlPool'],\
                    self.data['oilPipelineType'], self.data['isPlantLeak'], self.data['isWaterSourceArea'],\
                    self.data['monitoringWellNumber'], self.data['isRoutineMonitoring'], self.data['psi'],\
                    self.data['extChar2'], self.data['unitFunctionary'], self.data['auditorName'], self.data['preparer'],\
                    self.data['preparerContactWay'], self.data['prepareDateDisplay'], self.data['prepareDate'] = line
                #print(self.data)
                self.post(self.data)
                self.number += 1

        print('<<<上传完毕！>>>\n共发布 {} 条记录'.format(self.number))
        print('上传成功{}条，失败{}条'.format(self.number-self.error_number, self.error_number))

#数据上传的入口
urls = 'http://114.251.10.55/GWISWeb/tbBusGasStationList/save'

#header头信息，cookie 值需要手动从浏览器登录获取
header = {
    'Cookie': '',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'
}


if __name__ == '__main__':
    po = Post(urls, header)
    po.start()
