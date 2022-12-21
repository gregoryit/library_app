# -*- coding: utf-8 -*-
import mysql.connector
import os
from time import sleep
from consts import sql_request
from utils import *

# test teamcity15

# password= 'hello_password'

while True:
    try:
        mydb = mysql.connector.connect(
            host="db",
            user="root",
            password=os.environ['MYSQL_PASSWORD'],
            database='db'
                )
        break
    except BaseException:
        print('Connection failed. Try again..')
        sleep(1)

cursor = mydb.cursor(prepared=True)
for req in sql_request:
    try:
        cursor.execute(req)

    except BaseException:
        print('error!!!', req)


text = '''Возможности приложения:
1 - добавление
2 - удаление
3 - изменение
4 - книгу к факультету
'''

while True:
    print(text)
    for i in tables:
        print(show_all(cursor, i))
    com = input()
    if com == '1':
        print(add_smth_console(cursor))
    elif com == '2':
        print(del_smth_console(cursor))
    elif com == '3':
        print(upd_smth_console(cursor))
    elif com == '4':
        print(many_relations_console(cursor))
    mydb.commit()
