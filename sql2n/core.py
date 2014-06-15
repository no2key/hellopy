import mysql.connector
from mysql.connector.errors import Error

__version__ = 0.1
__author__ = 'imaguowei@gmail.com'


def get_version():
    return __version__


class GreenSql():
    conn = ''

    def __init__(self, host, user, password, database, autocommit=True, buffered=True):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.autocommit = autocommit
        self.buffered = buffered
        GreenSql.conn = self._connect()

    @staticmethod
    def get_connect():
        if not GreenSql.conn:
            raise Error('database connect error!')
        return GreenSql.conn

    def _connect(self):
        return mysql.connector.connect(host=self.host, user=self.user, password=self.password, database=self.database,
                                       autocommit=self.autocommit, buffered=self.buffered)

    def _close(self):
        pass


class Model():
    def __init__(self):
        self.db = GreenSql.get_connect()
        self.select_object = SelectObject(self)

    def get_by_id(self, mid):
        self.where('id =' + str(mid))
        return self.find_one()

    def find_one(self):
        cur = self.db.cursor()
        cur.execute(self.select_object.get_sql())
        result = cur.fetchone()
        cur.close()
        return result

    def select(self):
        cur = self.db.cursor()
        cur.execute(self.select_object.get_sql())
        result = cur.fetchall()
        cur.close()
        return result

    def insert(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def fm(self, fm):
        self.select_object.fm = fm
        return self

    def where(self, where):
        self.select_object.where = ' WHERE ' + where
        return self

    def join(self):
        pass

    def order_by(self, order):
        pass

    def limit(self, start=1, number=''):
        if number:
            limit = ' LIMIT ' + str(start) + ', ' + str(number)
        else:
            limit = ' LIMIT ' + str(start)
        self.select_object.limit = limit
        return self

    def create_table(self):
        CreateTable().create_table(self)

    def __str__(self):
        return str(self.select_object)


class SqlObject():
    def __init__(self, model):
        self.table_name = model.__class__.__name__.lower()

    def get_sql(self):
        pass

    def __str__(self):
        """打印类名和生成的sql语句"""
        return self.__class__.__name__ + '@' + self.get_sql()


class SelectObject(SqlObject):
    def __init__(self, model):
        self.fm = ''
        self.where = ''
        self.limit = ''
        self.sql = ''
        SqlObject.__init__(self, model)

    def get_sql(self):
        self.sql = 'SELECT * FROM '
        if not self.fm:
            self.fm = self.table_name
        self.sql += self.fm
        if self.where:
            self.sql += self.where
        if self.limit:
            self.sql += self.limit
        return self.sql


class DeleteObject(SqlObject):
    pass


class UpdateObject(SqlObject):
    pass


class InsertObject(SqlObject):
    pass


class Field():
    field_type = 'varchar'

    def __init__(self, default=''):
        self.default = default


class CharField(Field):
    field_type = 'varchar'


class IntField(Field):
    field_type = 'int'


class TextField(Field):
    field_type = 'text'


class DataTimeField(Field):
    field_type = 'datetime'


class EmailField(Field):
    field_type = 'email'


class PrimaryKey(Field):
    pass


class ForeignKeyField(Field):
    pass


class CreateTable():
    table_name = ''

    def __init__(self):
        pass

    def create_table_sql(self):
        pass

    def create_table(self, model):
        self.table_name = model.__class__.__name__.lower()