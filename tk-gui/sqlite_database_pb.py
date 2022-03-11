import sqlite3
import sys
import os

DB_NAME = 'phone_book.db'
DB_PATH = os.path.join( os.getcwd(), DB_NAME )
# if db does not exist, exit instead of creating one
if not os.path.exists(DB_PATH):
    sys.exit(f"database does not exist. lookup failed for - {DB_PATH}")

con = sqlite3.connect(DB_NAME)
cursorObj = con.cursor()


def sql_fetch():
    cursorObj.execute('SELECT id, name, phone, homephone, address FROM phone_book')

    rows = cursorObj.fetchall()

    return rows

def new(name, ph, hphone, add):
    query = f"INSERT INTO phone_book (name, phone, homephone, address) VALUES('{name}', {ph}, {hphone}, '{add}')"
    print(query)
    cursorObj.execute(query)
    con.commit()

def edit(id, name, ph, hphone, add):
    cursorObj = con.cursor()
    query = f'UPDATE phone_book SET name = "{name}", phone = "{ph}", homephone = "{hphone}", address = "{add}" where id = {id}'
    print(query)
    cursorObj.execute(query)
    con.commit()

def delete(id):
    cursorObj = con.cursor()
    query = f'DELETE FROM phone_book WHERE id = {id}'
    print(query)
    cursorObj.execute(query)
    con.commit()

# if __name__ == '__main__':
#     new('a', 'b', 'c', 'd')
