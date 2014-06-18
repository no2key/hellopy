"""supervisor 配置文件自动生成工具
"""


class Supervisor():
    def __init__(self, group, program, port, num):
        self.group = group
        self.program = program
        self.port = port
        self.num = num
        self.programs = []

    def mk_group(self):
        return '[group:{}]'.format(self.group)

    def mk_programs(self):
        res = ('programs=' + '{}, ' * self.num)[:-2]
        for i in range(self.num):
            self.programs.append(self.program + '-' + str(self.port + i))
        return res.format(*self.programs)


if __name__ == '__main__':
    sup = Supervisor('tornados', 'tornado', 8000, 4)
    print(sup.mk_group())
    print(sup.mk_programs())
    print(sup.programs)
