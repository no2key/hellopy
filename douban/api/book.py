from urllib.request import urlopen


class Book():
    url = 'https://api.douban.com/v2/book/'

    def _get(self, q):
        res = urlopen(self.url + str(q)).read().decode()
        return res

    def get_book_by_id(self, bid):
        return self._get(bid)

    def get_book_by_isbn(self, isbn):
        self.url += 'isbn/'
        return self._get(isbn)

    def search_book(self, name):
        pass


if __name__ == '__main__':
    print(Book().get_book_by_id(1003078))
    print(Book().get_book_by_isbn(9787544708531))