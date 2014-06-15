"""斐波那契数列
"""


def fib(num):
    a, b = 0, 1
    while a < num:
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    # for i in fib(10):
    #     print(i)

    f = fib(9)
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))

    s = sum(list(fib(1000000)))
    print(s)