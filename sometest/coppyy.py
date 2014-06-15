"""浅层拷贝与深层拷贝

"""

import copy


a = [{'name': 'jim'}, 'abc']

b = a
#直接赋值，两个引用指向同一对象

b[0]['name'] = 'tim'
print(a is b)


c = a.copy()
#浅层拷贝
c[0] = 'kik'
print(a, c)


d = copy.deepcopy(a)
#深层拷贝
d[0]['name'] = 'lll'
print(a, d)


