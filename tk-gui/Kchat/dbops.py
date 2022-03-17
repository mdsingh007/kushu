import sqlite3
import sys
import os

DB_NAME = 'kchat.db'
DB_PATH = os.path.join( os.getcwd(), 'Kchat', DB_NAME )
# if db does not exist, exit instead of creating one
if not os.path.exists(DB_PATH):
    sys.exit(f"database does not exist. lookup failed for - {DB_PATH}")
else:
    print (f'connecting to {DB_PATH}')

con = sqlite3.connect(DB_PATH)

def execute_sql(query):
    cursorObj = con.cursor()
    # print(query)
    cursorObj.execute(query)
    con.commit()
    return cursorObj

def select_all():
    sql = 'select * from chats'
    return execute_sql(sql).fetchall()


def new(sender, receiver, message):
    sql = f"INSERT INTO chats (sender, receiver, message) VALUES('{sender}', '{receiver}' , '{message}')"
    execute_sql(sql)


# if __name__ == '__main__':
#     select_all()