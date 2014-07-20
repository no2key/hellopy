# -*- coding:utf-8 -*-
import itertools
from functools import reduce
import redis
import pymysql


class AutoCpmplate():
    def __init__(self):
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0)
        self.db = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', database='zhengxing',
                                  charset='utf8')

    def add_all(self):
        cursor = self.db.cursor()
        cursor.execute('select name from api_doctor')
        for i in cursor:
            self.add(i[0])

    # def add(self, d):
    #     for i in range(1, len(d[1])+1):
    #         # self.r.sadd(d[1][0:i], d[2])
    #         self.r.sadd(d[1][0:i], d[1])
    #         # print(d[1][0:i])

    def add(self, s):
        keys = self.get_keys(s)
        for i in keys:
            self.r.sadd(i, s)

    def get_keys(self, s):
        """ 取得所有键
        对于输入'abc', 返回[a,b,c,ab,ac,bc,abc]

        :param s:
        :return:
        """
        data = []
        for i in range(1, len(s)+1):
            keys = list(itertools.combinations(s, i))
            for key in keys:
                data.append(reduce(lambda x, y: x+y, key))

        return data

    def query(self, s):
        return self.r.sdiff(s)

    def query_and_print(self, s):
        for k in auto.query(s):
            print(k.decode())


if __name__ == '__main__':
    auto = AutoCpmplate()
    # auto.add_all()
    # for j in auto.query('王明'):
    #     print(j.decode())
    auto.query_and_print('王明')
