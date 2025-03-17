import sqlite3
import function

conn=sqlite3.connect("sqlite.db")
print("Connection: ",conn)
cursor=conn.cursor()
print("Cursor: ",cursor)

query="select * from demo"
cursor.execute(query)

# Fetch one row
print("fetching one row")
row=cursor.fetchone()
print(row)
row=cursor.fetchone()
print(row)

# Fetch many
print("Fetching 3 rows")
# row=cursor.fetchmany(3)
# for r in row:
#   print(r)
function.query_responder(cursor,"fetchmany",3)

# Fetch all
print("fetching all is comming")
# rows=cursor.fetchall()
# for r in rows:
#     print(r)

function.query_responder(cursor,"fetchall")

query2="Insert into demo (Name,Hint) values ('Fitsum','First Name')"
cursor.execute(query2)

print("...............................")
id=int(input("Enter an id: "))
query3="select * from demo where ID >?"
cursor.execute(query3,(id,))
function.query_responder(cursor,"fetchall")

conn.close()