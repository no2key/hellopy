class Post():
    @staticmethod
    def count():
        with open('d.txt', 'rb') as f:
            for line in f:
                code1, quxian, code2 = line.strip().decode().split(':')
                #print(quxian)
                with open("dishi.txt", 'rb') as f2:
                    ls = [line.strip().decode() for line in f2]
                    for i in range(ls.count(quxian)+1):
                        if code1 == '':
                            print('::')
                        print('{}:{}:{}'.format(code1, quxian, code2))

    @staticmethod
    def post():
        pass

Post.count()