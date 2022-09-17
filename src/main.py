import mysql.connector
import os
from time import sleep

# while True:
#     try:
#         mydb = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password=os.environ['MYSQL_PASSWORD'],
#         database='db'
#         )
#         break
#     except:

#         print('Connection failed. Try again..')
#         sleep(1)

# cursor = mydb.cursor()

# while True:
#     cursor.execute('select * from books')
#     res = cursor.fetchall()
#     print(res)
#     input('press enter ')