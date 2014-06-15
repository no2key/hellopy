"""百度翻译api简单封装

默认设置为自动识别源语言
自动识别的规则：
当源语言为非中文时，目标语言自动设置为中文。当源语言为中文时，目标语言自动设置为英文。
如下例：
1）源语言识别为中文，则翻译方向为“中 -> 英”
2）源语言识别为英文，则翻译方向为“英 -> 中”
3）源语言识别为日文，则翻译方向为“日 -> 中”
"""

import json
from urllib.request import urlopen
from urllib.parse import urlencode


class BaiduTranslate():
    """百度翻译
    """
    #翻译接口地址
    url = 'http://openapi.baidu.com/public/2.0/bmt/translate?'

    def __init__(self, client_id, q='', fm='auto', to='auto'):
        #Baidu API Key
        self.client_id = client_id
        #源语言语种
        self.fm = fm
        #目标语言语种
        self.to = to
        #要翻译的原文
        self.q = q

    def get_url(self):
        """
        获取查询结果返回地址
        """
        data = {
            'client_id': self.client_id,
            'from': self.fm,
            'to': self.to,
            'q': self.q,
        }
        return BaiduTranslate.url + urlencode(data)

    def translate(self, q, fm='auto', to='auto'):
        self.fm = fm
        self.to = to
        self.q = q
        response = urlopen(self.get_url())
        result = json.loads(response.read().decode())
        if result.get('error_code', None):
            #当发生错误是抛出异常
            raise Exception(result['error_msg'])
        else:
            return result['trans_result'][0]['dst']


if __name__ == '__main__':
    #使用示例
    t = BaiduTranslate('填入你的api key').translate('hello world')
    print(t)