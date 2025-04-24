import sqlite3


conn = sqlite3.connect("datafile.db")
cursor = conn.cursor()

# Create Database & Insert data
cursor.execute(
    "create table people (id integer primary key, name text, count integer)""")
cursor.execute(
    "insert into people (name, count) values ('Ray', 25)")
cursor.execute(
    "insert into people (name, count) values ('Danny', 26)")
cursor.execute(
    "insert into people (name, count) values ('Woody', 28)")

# Read Database & Select data
result = cursor.execute(
    "select * from people where name='Ray'")
print(result.fetchall())

# Update data
cursor.execute("update people set count =? where name = ?", (30, 'Woody'))
result = cursor.execute("select * from people")
print(result.fetchall())

# Delete data
cursor.execute("Delete from people where name='Danny'")
result = cursor.execute("select * from people")
print(result.fetchall())

# Search data
name = input("Plz type the name you want to search:")
result = cursor.execute("select * from people where name = ?", (name,))
print(result.fetchall())

conn.commit()  # 儲存
conn.close()
