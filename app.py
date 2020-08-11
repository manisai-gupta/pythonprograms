from flask import Flask
from flask_cors import CORS
import sqlite3
import json

app = Flask(__name__)
CORS(app)

#img='https://i.pinimg.com/736x/29/b5/c5/29b5c52680f921fb3f8fee2817d1f63a.jpg'

@app.route('/')
def hello(enteryurname):
    return "Hello World!"
    #return img
    

@app.route('/createdb/<dbname>')
def create(dbname):
    conn = sqlite3.connect(dbname+'.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE todos
                 (todo text)''')
    conn.commit() 
    conn.close()    
    return "database created"

@app.route('/insertdb/<todo>/')
def insert(todo):
    conn = sqlite3.connect('mytodos.db')
    c = conn.cursor()
    c.execute("INSERT INTO todos VALUES ('"+todo+"')")
    #print(todo, "is inserted")
    conn.commit()
    conn.close()
    return "SUCCESS"

@app.route('/gettodos/')
def gettodos():
    conn = sqlite3.connect('mytodos.db')
    c = conn.cursor()
    c.execute("SELECT rowid, todo FROM todos")
    # c.execute("UPDATE todos SET todo = 'My First Task' WHERE rowid = 1")
    todos = c.fetchall()
    todo_array = []
    for t in todos:
        todo_array.append(t)
    return json.dumps(todo_array)

@app.route('/deletetodos/<deleteelement>')
def deletetodos(deleteelement):
    conn=sqlite3.connect("mytodos.db")
    c=conn.cursor()
    c.execute("DELETE FROM todos WHERE rowid='"+deleteelement+"'")
    conn.commit()
    conn.close()
    return "record deleted"


@app.route('/updatetodos/<updatenewvalue>/<selectrowid>')
def updatetodos(updatenewvalue,selectrowid):
    conn = sqlite3.connect('mytodos.db')
    c = conn.cursor()
    c.execute("UPDATE todos SET todo = '"+updatenewvalue+"' WHERE rowid = '"+selectrowid+"'")
    conn.commit()
    conn.close()
    return "updated value"
app.run(port="1309")