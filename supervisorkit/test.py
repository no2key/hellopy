import unittest
from supervisorkit.confcc import Supervisor


class TestSupervisor(unittest.TestCase):

    def setUp(self):
        self.supervisor = Supervisor('tornados', 'tornado', 8000, 4)

    def test_mk_group(self):
        self.assertEqual('[group:tornados]', self.supervisor.mk_group())

    def test_mk_programs(self):
        self.assertEqual('programs=tornado-8000, tornado-8001, tornado-8002, tornado-8003', self.supervisor.mk_programs())
        self.assertListEqual(['tornado-8000', 'tornado-8001', 'tornado-8002', 'tornado-8003'], self.supervisor.programs)
