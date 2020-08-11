from flask import Flask
import sqlite3

app=Flask(__name__)

@app.route('/createdb/<dbname>/insertdb/<todo>/gettodos/')
def data(dbname,todo):
    conn = sqlite3.connect(dbname+'.db')
    c = conn.cursor()
    #c.execute('''CREATE TABLE todos
    #             (todo text)''')
    #conn.commit()            
   #todo = input("Enter todo: ")
    c.execute("INSERT INTO todos VALUES ('"+todo+"')")
    #print(todo, "is inserted")
    c.execute("SELECT rowid,todo FROM todos")
    todos = c.fetchall()
   #print(todos)
    for t in todos:
        print(t)
    conn.commit()
    conn.close()
    return str(todos)

app.run()