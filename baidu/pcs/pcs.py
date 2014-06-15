"""
目前百度PCS api临时关闭新的开启
doc: http://developer.baidu.com/wiki/index.php?title=docs/pcs/rest/file_data_apis_list
"""

import json
from urllib.parse import urlencode
from urllib.request import urlopen


class Pcs():
    def __init__(self, access_token):
        self.access_token = access_token

    def upload(self, path, file):
        """单文件上传
        """
        url = 'https://c.pcs.baidu.com/rest/2.0/pcs/file'
        data = {
            'method': 'upload',
            'access_token': self.access_token,
            'path': path,
            'file': file,
            #覆盖同名文件
            'ondup': 'overwrite',
        }

        response = urlopen(url, urlencode(data))
        return json.loads(response.read().decode())

    def download(self, path):
        """单文件下载
        """
        url = 'https://d.pcs.baidu.com/rest/2.0/pcs/file?'
        data = {
            'method': 'download',
            'access_token': self.access_token,
            'path': path
        }

        return url + urlencode(data)

    def mkdir(self, path):
        url = 'https://pcs.baidu.com/rest/2.0/pcs/file'
        data = {
            'method': 'mkdir',
            'access_token': self.access_token,
            'path': path,
        }

        response = urlopen(url, urlencode(data))
        return json.loads(response.read().decode())

#todo more methods
