from consts import tables
import logging


logging.basicConfig(filename='all.log', encoding='utf-8', level=logging.DEBUG)




from fluent import sender
from fluent import event


logger = sender.FluentSender('app', host='localhost', port=24224)


def add_smth_console(cursor):
    print(*tables.keys())
    ans = input('Что добавить?')
    if ans in tables.keys():
        print('Введите', *tables[ans][1:], 'через пробел')
        values = input().split()
        add_smth(cursor, values, ans)


def add_smth(cursor, values, ans):
    try:
        sss = ', '.join(['%s'] * (len(tables[ans])-1))
        cols = ", ".join(tables[ans][1:])
        sql = f'INSERT INTO {ans} ({cols}) VALUES ({sss});'
        values = [i if i != 'None' else None for i in values]
        cursor.execute(sql, tuple(values))
        sql = f'SELECT MAX(id) FROM {ans}'
        cursor.execute(sql)
        id_new = cursor.fetchone()[0]
        sql = f'SELECT * FROM {ans} WHERE id = %s'
        cursor.execute(sql, tuple([id_new]))
        logging.info(f'Добавление записи в {ans} в параметрами {values}')
        logger.emit('app', {
                'action': 'add',
                'table': ans,
                'values': values
                })
        return cursor.fetchall()[0]
    except Exception as e:
        logging.error(f'Добавление записи в {ans} в параметрами {values} не удалось')
        print('Что-то пошло не так')


def del_smth_console(cursor):
    print(*tables.keys())
    ans = input('Где удалить? ')
    if ans in tables.keys():
        print(f'Строки в таблице {ans}:')
        print(show_all(cursor, ans))
        print('Введите id для удаления')
        id_del = input()
        del_smth(cursor, id_del, ans)


def del_smth(cursor, id_del, ans):
    try:
        sql = f'DELETE FROM {ans} WHERE id = %s;'
        cursor.execute(sql, tuple([id_del]))
        sql = f'SELECT id FROM {ans} WHERE id = %s'
        cursor.execute(sql, tuple([id_del]))
        result = cursor.fetchall()
        logging.info(f'Удаление записи в {ans} в id {id_del}')
        logger.emit('app', {
                'action': 'del',
                'table': ans,
                'id': id_del
                })
        return result
    except Exception as e:
        logging.error(f'Удаление записи в {ans} в id {id_del} не удалось')
        print('Что-то пошло не так')


def upd_smth_console(cursor):
    print(*tables.keys())
    ans = input('Где изменить?')
    if ans in tables.keys():
        print(f'Строки в таблице {ans}:')
        print(show_all(cursor, ans))
        print('Введите id для изменения')
        id_del = input()
        print('Введите поле для изменения')
        col = input()
        print('Введите новое значение')
        value = input()
        if col in tables[ans][1:]:
            upd_smth(cursor, ans, id_del, col, value)


def upd_smth(cursor, ans, id_del, col, value):
    try:
        sql = f'UPDATE {ans} SET {col} = %s WHERE id = %s;'
        cursor.execute(sql, tuple([value, id_del]))
        sql = f'SELECT * FROM {ans} WHERE id = %s'
        cursor.execute(sql, tuple([id_del]))
        logging.info(f'Изменение записи в {ans} в id {id_del} параметр {col} на значение {value}')
        logger.emit('app', {
                'action': 'upd',
                'table': ans,
                'id': id_del,
                'parametr': col,
                'value': value
                })
        return cursor.fetchall()[0]
    except Exception as e:
        print('Что-то пошло не так')
        logging.error(f'Изменение записи в {ans} в id {id_del} параметр {col} на значение {value} не удалось')


def many_relations_console(cursor):
    print('Строки в таблице книг:')
    print(show_all(cursor, 'books'))
    print('Строки в таблице факультетов:')
    print(show_all(cursor, 'facilities'))

    b = input('Какая книга? ')
    f = input('Какой филиал? ')
    many_relations(cursor, b, f)


def many_relations(cursor, b, f):
    try:
        sql = f'INSERT INTO books_facilities VALUES (%s, %s);'
        cursor.execute(sql, tuple([f, b]))
    except Exception as ex:
        print('Что-то пошло не так')


def show_all(cursor, tab):
    cursor.execute(f'select * from {tab}')
    res = cursor.fetchall()
    return res


def create(cursor, table, num, values):
    cols = ", ".join(tables[table][1:])
    sss = ", ".join(["%s"] * num)
    sql = f'INSERT INTO {table} ({cols}) VALUES ({sss});'
    cursor.execute(sql, values)
    sql = f'SELECT * FROM {table} WHERE id = 1'
    cursor.execute(sql)
    return cursor.fetchall()[0]
