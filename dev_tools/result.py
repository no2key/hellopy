"""格式化json返回
"""

import json


def result(data, status='success', message=''):
    data = {
        'status': status,
        'message': message,
        'results': data
    }
    return json.dumps(data)


if __name__ == '__main__':
    d = {
        'name': 'jim',
        'age': 12,
    }
    r = result(d)
    print(r)

