"""重载字典下标操作符，使字典get忽略大小写
"""


class IDict(dict):
    def __getitem__(self, item):
        return self.get(item.lower())


a = IDict()

a['a'] = 'aaa'

print(a['A'])
