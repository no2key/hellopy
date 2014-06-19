import unittest
from supervisorkit.confcc import Supervisor


class TestSupervisor(unittest.TestCase):

    def setUp(self):
        self.supervisor = Supervisor('tornados', 'tornado', 8000, 4, '/home/maguowei/tornado', 'bastogne.py')

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
        with open('supervisor.conf', 'w') as f:
            f.write(self.supervisor.mk_group())
            f.write(self.supervisor.mk_programs())
            for p in self.supervisor.get_all_programs():
                f.write(p)

        self.assertListEqual([], self.supervisor.get_all_programs())
