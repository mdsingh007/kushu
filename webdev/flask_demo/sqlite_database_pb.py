import sqlite3
import sys
import os

DB_NAME = 'phone_book.db'
DB_PATH = os.path.join( os.getcwd(), DB_NAME )
# if db does not exist, exit instead of creating one
if not os.path.exists(DB_PATH):
    sys.exit(f"database does not exist. lookup failed for - {DB_PATH}")


def execute_sql(query):
    con = sqlite3.connect(DB_NAME)
    cursorObj = con.cursor()
    print(query)
    cursorObj.execute(query)
    con.commit()
    return cursorObj

def sql_fetch(whclause = ''):
    if whclause != '':
        cur = execute_sql(f'SELECT * FROM phone_book WHERE name like "%{whclause}%" OR address like "%{whclause}%"')
    else:
        cur = execute_sql('SELECT id, name, phone, homephone, address FROM phone_book')
    
    rows = cur.fetchall()
    return rows

def get_by_id(id):
    data = execute_sql(f"SELECT * FROM phone_book WHERE id={id}").fetchall()
    return data[0]

def new(name, ph, hphone, add):
    execute_sql(f"INSERT INTO phone_book (name, phone, homephone, address) VALUES('{name}', {ph}, {hphone}, '{add}')")

def edit(id, name, ph, hphone, add):
    execute_sql(f'UPDATE phone_book SET name = "{name}", phone = "{ph}", homephone = "{hphone}", address = "{add}" where id = {id}')

def delete(id):
    execute_sql(f'DELETE FROM phone_book WHERE id = {id}')

def sql_fetch2():
    cur = execute_sql('SELECT id, author, kweet, postedon FROM kwitter')
    rows = cur.fetchall()
    return rows

def get_by_author(author):
    data = execute_sql(f"select kwitter.kweet, kwitter.postedon, users.name, users.picture from kwitter  join users ON kwitter.userid = users.id where users.name = '{author}'").fetchall()
    return data

def get_kweeters():
    data = execute_sql("SELECT name FROM users").fetchall()
    return data

def new_kweet(new_kweet, userid, postedon):
    execute_sql(f"INSERT INTO kwitter (kweet, postedon, userid) VALUES('{new_kweet}', '{userid}', '{postedon}')")

# if __name__ == '__main__':
#     new('a', 'b', 'c', 'd')
