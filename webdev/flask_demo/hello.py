import sys
from flask import Flask, request
import sqlite_database_pb as db
from flask import render_template


app = Flask(__name__)


@app.route("/tmpl/")
def hello_world2():
    search = request.args.get('search')
    if search and search != None:
        data = db.sql_fetch(search)
    else:
        data = db.sql_fetch()
    return render_template('hello.html', data = data)

@app.route("/edit/")
def edit():
    id = request.args.get('id')
    # print(key, file=sys.stdout)
    # variables = {"name": "Kushagra"}
    pb_data = ""
    if id == None:
        print("new", file=sys.stdout)
    else:
        print("edit", file=sys.stdout)
        pb_data = db.get_by_id(id)
    return render_template('edit.html', data = pb_data)

@app.route("/edit_submit/")
def edit_submit():
    id = request.args.get('id')
    name = request.args.get('name')
    phone = request.args.get('phone')
    homephone = request.args.get('home_phone')
    address = request.args.get('address')
    dr_id = request.args.get('dr_id')
    try:
        if name == "" or phone == "" or homephone == "" or address == "":
            return "Please <a href='/edit/'>fill in all the boxes</a>"
        else:
            if id and id != None:
                db.edit(id, name, phone, homephone, address)
            elif dr_id and dr_id != None:
                db.delete(dr_id)
            else:
                db.new(name, phone, homephone, address)
            return "YAY! Your entry is saved. Go to <a href='/tmpl/'>home page</a>"
    except:
        return "Phone numbers can only have numbers, please <a href='/edit/'>try again</a>"


@app.route("/")
def hello_world():
    data = db.sql_fetch()
    rows = []
    for elem in data:
        row = f"<tr><td>{elem[0]}</td><td>{elem[1]}</td><td>{elem[2]}</td><td>{elem[3]}</td><td>{elem[4]}</td></tr>"
        rows.append(row)

    rows = "".join(rows)

    html = f'''
    <table border='4px'>
        <tr>
            <th>Id</th>
            <th>Name</th>
            <th>Phone</th>
            <th>Home Phone</th>
            <th>Address</th>
        </tr>
        {rows}
    </table>
    '''

    return html




# def hello_world():
#     data = db.sql_fetch()
#     data2 = []
#     for elem in data:
#         for elem2 in elem:
#             data2.append(str(elem2))
#         data2.append("    |    ")
#     return " ".join(data2[0:-1]) C:\Programming\GitHub\kushu\webdev\flask_demo\hello.py