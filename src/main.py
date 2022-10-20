# -*- coding: utf-8 -*-
import mysql.connector
import os
from time import sleep

#test teamcity9

while True:
    try:
        mydb = mysql.connector.connect(
        host="db",
        user="root",
        password=os.environ['MYSQL_PASSWORD'],
        database='db'
        )
        break
    except:

        print('Connection failed. Try again..')
        sleep(1)

cursor = mydb.cursor()
try:
    cursor.execute("""CREATE TABLE books (
                    idbooks INT NOT NULL AUTO_INCREMENT,
                    title VARCHAR(45) NULL,
                    PRIMARY KEY (idbooks));
                    """)
except:
    print('error!!!')

while True:
    book = input('Какую книгу вы хотите добавить? ')
    cursor.execute(f""" INSERT INTO books (title) VALUES ('{book}');
                """)
    mydb.commit()
    cursor.execute('select * from books')
    res = cursor.fetchall()
    print(res)