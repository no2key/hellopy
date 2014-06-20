import unittest
from supervisorkit.confcc import Supervisor


class TestSupervisor(unittest.TestCase):

    conf = {
        'group': 'tornados',
        'program': 'tornado',
        'port': 8000,
        'num': 4,
        'directory': '/home/maguowei/tornado',
        'command': 'bastogne.py',
    }

    def setUp(self):
        self.supervisor = Supervisor(**self.conf)

    def test_mk_group(self):
        self.assertEqual('[group:tornados]', self.supervisor.mk_group())

    def test_mk_programs(self):
        self.assertEqual('programs=tornado-8000, tornado-8001, tornado-8002, tornado-8003', self.supervisor.mk_programs())
        self.assertListEqual(['tornado-8000', 'tornado-8001', 'tornado-8002', 'tornado-8003'], self.supervisor.programs)

    def test_mk_program(self):
        res = """
[program:tornado-8000]
command=python3 /home/maguowei/tornado/bastogne.py --port=8000
directory=/home/maguowei/tornado
autorestart=true
redirect_stderr=true
stdout_logfile=/var/log/tornado/tornado@8000.log
loglevel=info
        """
        self.assertEqual(res, self.supervisor.mk_program(8000))

    def test_get_all_programs(self):
        res = []
        for i in range(self.conf['num']):
            res.append(self.supervisor.mk_program(self.conf['port'] + i))
        with open('supervisor.conf', 'w') as f:
            f.write(self.supervisor.mk_group() + '\n')
            f.write(self.supervisor.mk_programs() + '\n')
            for p in self.supervisor.get_all_programs():
                f.write(p)

        self.assertListEqual(res, self.supervisor.get_all_programs())
