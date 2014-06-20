"""supervisor 配置文件自动生成工具
"""


class Supervisor():
    def __init__(self, group, program, port, num, directory, command):
        self.group = group
        self.program = program
        self.port = port
        self.num = num
        self.directory = directory
        self.command = command
        self.programs = []

    def mk_group(self):
        return '[group:{}]'.format(self.group)

    def mk_programs(self):
        res = ('programs=' + '{}, ' * self.num)[:-2]
        for i in range(self.num):
            self.programs.append(self.program + '-' + str(self.port + i))
        return res.format(*self.programs)

    def mk_program(self, port):
        res = """
[program:{program}-{port}]
command=python3 {directory}/{command} --port={port}
directory={directory}
autorestart=true
redirect_stderr=true
stdout_logfile=/var/log/{program}/{program}@{port}.log
loglevel=info
        """
        return res.format(program=self.program, port=port, directory=self.directory, command=self.command)

    def get_all_programs(self):
        res = []
        for i in range(self.num):
            res.append(self.mk_program(self.port + i))

        return res