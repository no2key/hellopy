with open("dict.txt", 'rb') as f:
    for line in f:
        x, y = line.decode().split(':')
        #print("self.data['{}']".format(x), end=', ')
        print("{},".format(y.strip()), end='')
