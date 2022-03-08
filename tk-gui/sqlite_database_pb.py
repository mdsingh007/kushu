import sqlite3

con = sqlite3.connect('phone_book.db')
cursorObj = con.cursor()


def sql_fetch():
    cursorObj.execute('SELECT * FROM phone_book')

    rows = cursorObj.fetchall()

    return rows

def new(name, ph, hphone, add):
    query = f"INSERT INTO phone_book (name, phone, homephone, address) VALUES('{name}', {ph}, {hphone}, '{add}')"
    print(query)
    cursorObj.execute(query)
    con.commit()

def edit(id, name, ph, hphone, add):
    cursorObj = con.cursor()
    cursorObj.execute(f'UPDATE phone_book SET name = "{name}", phone = "{ph}", hphone = "{hphone}", address = "{add}" where id = {id}')
    con.commit()

# if __name__ == '__main__':
#     new('a', 'b', 'c', 'd')
