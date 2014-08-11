from hello_celery.tasks import add


if __name__ == '__main__':
    res = add.delay(2, 4)
    res1 = add.delay(2, 3)
    print(res.status)
    print(res1.status)
