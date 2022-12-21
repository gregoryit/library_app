import unittest
import mysql.connector
from utils import *
from consts import *
from test_db import MockDB
from mock import patch
import utils


class TestUtilsIntegr(MockDB):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.publisher = create(cls.cursor, 'publishers', 1, ('name_t_pub',))
        cls.filial = create(cls.cursor, 'filials', 2,
                            ('name_t_fil', 'addr_t_fil'))
        cls.facility = create(cls.cursor, 'facilities', 1, ('name_t_fac',))
        cls.book = create(cls.cursor, 'books', 4,
                          ('title_t', 'author_t', 1, 1))
        create(cls.cursor, 'publishers', 1, ('name_t_pub_deleting',))
        create(cls.cursor, 'filials', 2,
               ('name_t_fil_deleting', 'addr_t_fil_deleting'))
        create(cls.cursor, 'facilities', 1, ('name_t_fac_deleting',))
        create(cls.cursor, 'books', 4,
               ('title_t_deleting', 'author_t_deleting', 1, 1))

    def test_add(self):
        tables = {
            'publishers': ('test_pub_name',),
            'facilities': ('test_fac_name',),
            'filials': ('test_fil_name', 'test_address',),
            'books': ('test_title', 'test_author', 1, 1),
        }
        for tab, values in tables.items():
            add_smth(self.cursor, values, tab)
            sql = f'SELECT MAX(id) FROM {tab}'
            self.cursor.execute(sql)
            id_new = self.cursor.fetchone()
            sql = f'SELECT * FROM {tab} WHERE id = %s'
            self.cursor.execute(sql, id_new)
            db = self.cursor.fetchall()[0]
            self.assertEqual(values, db[1:])

    def test_update(self):
        tables_new = {
            'books': ('title', 'new_title', 1),
            'publishers': ('name', 'new_name', 1),
            'facilities': ('name', 'new_name', 1),
            'filials': ('name', 'new_name', 1),
        }
        for tab, values in tables_new.items():
            upd_smth(self.cursor, tab, 1, values[0], values[1])
            sql = f'SELECT * FROM {tab} WHERE id = 1'
            self.cursor.execute(sql)
            db = self.cursor.fetchall()[0]
            index = values[2]
            self.assertEqual(db[index], values[1])

    def test_delete(self):
        tables = {
            'books': 2,
            'publishers': 2,
            'facilities': 2,
            'filials': 2,
        }
        for tab, value in tables.items():
            del_smth(self.cursor, value, tab)
            sql = f'SELECT * FROM {tab} WHERE id = %s'
            self.cursor.execute(sql, (value,))
            result = self.cursor.fetchall()
            self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
