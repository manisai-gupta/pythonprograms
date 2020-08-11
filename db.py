import sqlite3

conn = sqlite3.connect('mytodos2.db')
c = conn.cursor()
#c.execute('''CREATE TABLE todos
#             (todo text)''')
#conn.commit()            
for i in range(5):
    todo = input("Enter todo: ")
    c.execute("INSERT INTO todos VALUES ('"+todo+"')")
print(todo, "is inserted")
c.execute("SELECT * FROM todos")
todos = c.fetchall()
print(todos)
#or t in todos:
#    print(t)
conn.commit()
conn.close()