"""使用redis实现自动补全

"""
import itertools
from functools import reduce
import redis


class AutoCpmplate():
    def __init__(self, host='localhost', port=6379, db=0):
        self.r = redis.StrictRedis(host=host, port=port, db=db)

    def add_all(self, l):
        for i in l:
            self.add(i)

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


if __name__ == '__main__':
    auto = AutoCpmplate()
    test_data = ['张三', '张三丰', '张学良']
    auto.add_all(test_data)
    for j in auto.r.sdiff('三'):
        print(j.decode())