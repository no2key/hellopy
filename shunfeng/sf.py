"""顺风快件查询

"""

import requests


class ShunFeng():
    url = 'http://www.sf-express.com/sf-service-web/service/bills/'

    def __init__(self, nummer):
        self.url = ShunFeng.url + '{}/routes?app=bill&lang=sc&region=cn&translate='.format(nummer)

    def get(self):
        response = requests.get(self.url)
        return response.json()

if __name__ == '__main__':
    n = input('输入订单号')
    print(ShunFeng(n).get())
