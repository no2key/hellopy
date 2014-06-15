"""豆瓣FM

"""

from urllib.request import urlopen, HTTPError
from urllib import parse
from json import JSONDecoder


class Fm():
    #认证地址
    login_url = 'http://www.douban.com/j/app/login'
    #频道地址
    channel_list_url = 'http://www.douban.com/j/app/radio/channels'
    #歌曲列表
    music_list = 'http://www.douban.com/j/app/radio/people'
    #登陆数据
    data = {
        'app_name': 'radio_desktop_win',
        'version': 100,
        'email': '',
        'password': '',
    }

    def __init__(self, email, password):
        self.data['email'] = email
        self.data['password'] = password
        self.data = parse.urlencode(self.data).encode()
        self.oauth = ''
        self.channel_list = ''
        self.get_token()
        self.get_channel_list()

    def get_token(self):
        try:
            r = urlopen(self.login_url, self.data)
            self.oauth = r.read().decode()
        except HTTPError as err:
            print(err)

    def get_channel_list(self):
        """获取频道列表

        """
        try:
            r = urlopen(self.channel_list_url)
            json = JSONDecoder()
            self.channel_list = json.decode(r.read().decode())
        except HTTPError as err:
            print(err)


if __name__ == '__main__':
    fm = Fm('imaguowei@gmail.com', '')
    channels = fm.channel_list['channels']
    for channel in channels:
        print(channel)