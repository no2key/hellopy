import uuid


def unique_id(num):
    while num > 0:
        yield uuid.uuid1()
        num -= 1


if __name__ == '__main__':
    a = unique_id(5)
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))