from consts import tables


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
        sql = f'INSERT INTO {ans} ({", ".join(tables[ans][1:]) }) VALUES ({sss});'
        values = [i if i != 'None' else None for i in values]
        cursor.execute(sql, tuple(values))
        sql = f'SELECT MAX(id) FROM {ans}'
        cursor.execute(sql)
        id_new = cursor.fetchone()[0]
        sql = f'SELECT * FROM {ans} WHERE id = %s'
        cursor.execute(sql, tuple([id_new]))
        return cursor.fetchall()[0]
    except:
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
        return result
    except:
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
        return cursor.fetchall()[0]
    except:
        print('Что-то пошло не так')


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
    except:
        print('Что-то пошло не так')    


def show_all(cursor, tab):
    cursor.execute(f'select * from {tab}')
    res = cursor.fetchall()
    return res


def create(cursor, table, num, values):
    sql = f'INSERT INTO {table} ({", ".join(tables[table][1:]) }) VALUES ({", ".join(["%s"] * num)});'
    cursor.execute(sql, values)
    sql = f'SELECT * FROM {table} WHERE id = 1'
    cursor.execute(sql)
    return cursor.fetchall()[0]
