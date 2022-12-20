from unittest import TestCase
import mysql.connector
from mysql.connector import errorcode
from mock import patch
import utils
from consts import *
import os


MYSQL_USER = "root"
MYSQL_PASSWORD = os.environ['MYSQL_PASSWORD']
MYSQL_DB = "testdb"
MYSQL_HOST = "db"
MYSQL_PORT = "3306"


class MockDB(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.cnx = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            port = MYSQL_PORT
        )
        cls.cursor = cls.cnx.cursor()

        # drop database if it already exists
        try:
            cls.cursor.execute("DROP DATABASE {}".format(MYSQL_DB))
            cls.cursor.close()
            print("DB dropped")
        except mysql.connector.Error as err:
            print("{}{}".format(MYSQL_DB, err))

        cls.cursor = cls.cnx.cursor()
        try:
            cls.cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(MYSQL_DB))
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            exit(1)
        cls.cnx.database = MYSQL_DB

        try:
            for query in sql_request:
                cls.cursor.execute(query)
                cls.cnx.commit()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("test_table already exists.")
            else:
                print(err.msg)
        else:
            print("OK")


        testconfig ={
            'host': MYSQL_HOST,
            'user': MYSQL_USER,
            'password': MYSQL_PASSWORD,
            'database': MYSQL_DB
        }
        # cls.mock_db_config = patch.dict(utils.config, testconfig)

    @classmethod
    def tearDownClass(cls):
        cls.cursor.fetchall()
        cls.cursor.close()
        cls.cnx.close()
        cnx = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD
        )
        cursor = cnx.cursor(dictionary=True)

        # drop test database
        try:
            cursor.execute("DROP DATABASE {}".format(MYSQL_DB))
            cnx.commit()
            cursor.close()
        except mysql.connector.Error as err:
            print("Database {} does not exists. Dropping db failed".format(MYSQL_DB))
        cnx.close()
