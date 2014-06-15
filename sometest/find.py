"""文件查找
"""

import glob
from sys import argv


def find():
    try:
        arg = argv[1]
    except IndexError:
        arg = '*'
    files = glob.glob(arg)

    for file in files:
        print(file)


if __name__ == '__main__':
    find()
