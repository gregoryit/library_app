import unittest
import mysql.connector
from utils import *
from consts import *
from test_db import MockDB


class TestUtils(MockDB):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.publisher = create(
            cls.cursor,
            'publishers',
            1,
            ('name_t_pub',)
        )
        cls.filial = create(
            cls.cursor,
            'filials',
            2,
            ('name_t_fil', 'addr_t_fil')
        )
        cls.facility = create(cls.cursor, 'facilities', 1, ('name_t_fac',))
        cls.book = create(cls.cursor, 'books', 4,
                          ('title_t', 'author_t', 1, 1))
        create(cls.cursor, 'publishers', 1, ('name_t_pub_deleting',))
        create(cls.cursor, 'filials', 2,
               ('name_t_fil_deleting', 'addr_t_fil_deleting'))
        create(cls.cursor, 'facilities', 1, ('name_t_fac_deleting',))
        create(cls.cursor, 'books', 4,
               ('title_t_deleting', 'author_t_deleting', 1, 1))

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def test_add(self):
        tables = {
            'books': ('test_title', 'test_author', 1, 1),
            'publishers': ('test_pub_name',),
            'facilities': ('test_fac_name',),
            'filials': ('test_fil_name', 'test_address',),
        }
        for tab, values in tables.items():
            result = add_smth(self.cursor, values, tab)[1:]
            for i in range(len(values)):
                self.assertEqual(result[i], values[i])

    def test_update(self):
        tables = {
            'books': ('title', 'new_title', 1),
            'publishers': ('name', 'new_name', 1),
            'facilities': ('name', 'new_name', 1),
            'filials': ('name', 'new_name', 1),
        }
        for tab, values in tables.items():
            result = upd_smth(self.cursor, tab, 1, values[0], values[1])
            index = values[2]
            self.assertEqual(result[index], values[1])

    def test_delete(self):
        tables_id = {
            'books': 2,
            'publishers': 2,
            'facilities': 2,
            'filials': 2,
        }
        for tab, value in tables_id.items():
            result = del_smth(self.cursor, value, tab)
            self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
