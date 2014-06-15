from http.cookiejar import CookieJar
from urllib.request import urlopen, build_opener, install_opener, Request, HTTPCookieProcessor
from urllib.parse import urlencode
from bs4 import BeautifulSoup


def get_html(url):
    response = urlopen(url)
    return response.read().decode()


def post_date(url, data):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36'
    }
    r = Request(url, data, headers)
    urlopen(r)


def set_cookies():
    set_cookies.cj = CookieJar()
    opener = build_opener(HTTPCookieProcessor(set_cookies.cj))
    install_opener(opener)


class Zhihu():
    url = 'http://www.zhihu.com/'
    login_url = url + 'login'

    def __init__(self, email='', password=''):
        self.email = email
        self.password = password

    def login(self, email, password):
        self.email = email
        self.password = password
        data = {
            'email': self.email,
            'password': self.password
        }
        post_date(self.login_url,  urlencode(data).encode())

    def search(self, q):
        url = self.url + 'search?'
        query = {
            'q': q,
            'type': 'question',
        }

        html = get_html(url + urlencode(query))
        result = BeautifulSoup(html)
        questions = result.find_all('a', class_='question_link')
        for q in questions:
            print(q.em.next_sibling.string, q['href'])


class User():
    def __init__(self, username='', url=''):
        self.username = username
        self.url = url

    def get_answers(self):
        html = get_html(self.url + '/answers')
        return html

    def get_asks(self):
        html = get_html(self.url + '/asks')
        soup = BeautifulSoup(html)
        asks = soup.find_all(class_='zm-profile-section-item zg-clear')
        return asks


if __name__ == '__main__':
    set_cookies()
    zhihu = Zhihu()
    zhihu.login('xxxxxxxx', 'xxxxxxxx')
    print(get_html('http://www.zhihu.com/inbox'))
    print(get_html(Zhihu.url))

