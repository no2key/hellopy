"""Python中的函数式编程

"""


#lambda 表达式
print('*' * 20)

a = lambda x, y: x + y
print(a(2, 3))

#带默认参数
b = lambda x=1, y=2: x + y
print(b())


# zip
print('*' * 20)

c = ['a', 'b', 'c']
d = [1, 3, 4]

e = dict(zip(c, d))
for i in e:
    print(i, e[i])


# map
print('*' * 20)


def inc(x):
    return x + 10

f = [1, 2, 3, 4]

g = list(map(inc, f))
print(g)


# filter
print('*' * 20)

h = [1, 2, 3, 4, 5]
i = filter(lambda x: x > 2, h)
print(list(i))


#reduce
print('*' * 20)

from functools import reduce

j = [1, 2, 3, 4, 5, 6]

k = reduce(lambda x, y: x + y, j)
print(k)