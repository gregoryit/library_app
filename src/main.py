# -*- coding: utf-8 -*-
import mysql.connector
import os
from time import sleep
from consts import sql_request
from utils import *
import logging
from fluent import sender
from fluent import event

from prometheus_client import start_http_server, Counter

ADD_REQUESTS = Counter('add_requests_total', 'total number of adding requests')
DEL_REQUESTS = Counter('del_requests_total', 'total number of deleting requests')
UPD_REQUESTS = Counter('upd_requests_total', 'total number of updating requests')
REL_REQUESTS = Counter('rel_requests_total', 'total number of relation requests')

start_http_server(8000)

logger = sender.FluentSender('app', host='localhost', port=24224)
# test teamcity33

# password= 'hello_password'

logging.basicConfig(filename='all.log', encoding='utf-8', level=logging.DEBUG)

while True:
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database='db'
                )
        break
    except BaseException:
        print('error')
    try:
        mydb = mysql.connector.connect(
            host="db",
            user="root",
            password="root",
            database='db'
                )
        break
    except BaseException:
        print('error')

cursor = mydb.cursor(prepared=True)
for req in sql_request:
    try:
        cursor.execute(req)

    except BaseException as e:
        # print('error!!!', req, e)
        print('error!!!')


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
        ADD_REQUESTS.inc()
        print(add_smth_console(cursor))
    elif com == '2':
        DEL_REQUESTS.inc()
        print(del_smth_console(cursor))
    elif com == '3':
        UPD_REQUESTS.inc()
        print(upd_smth_console(cursor))
    elif com == '4':
        REL_REQUESTS.inc()
        print(many_relations_console(cursor))
    mydb.commit()
