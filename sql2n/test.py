import unittest
from sql2n.core import *


class User(Model):
    username = CharField()
    password = CharField()
    email = CharField()
    reg_date = DataTimeField()

GreenSql('localhost', 'root', 'root', 'test')


class TestGreenSql(unittest.TestCase):
    def setUp(self):
        pass


class TestSelectObject(unittest.TestCase):
    def setUp(self):
        pass

    def test_self(self):
        self.assertEqual('SelectObject@SELECT * FROM user', str(User()))

    def test_fm(self):
        self.assertEqual('SelectObject@SELECT * FROM post', str(User().fm('post')))

    def test_limit(self):
        self.assertEqual('SelectObject@SELECT * FROM user LIMIT 3', str(User().limit(3)))

    def test_where(self):
        self.assertEqual('SelectObject@SELECT * FROM user WHERE id=1', str(User().where('id=1')))

    def test_select_object(self):
        self.assertEqual('SelectObject@SELECT * FROM post WHERE id=2 LIMIT 2, 4', str(User()
        .fm('post').where('id=2').limit(2, 4)))