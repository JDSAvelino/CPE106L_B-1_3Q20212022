import sqlite3 as sql

db = sql.connect("Machine Problem 3.db")
cursor =db.cursor()

cursor.execute("Select name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())

print("\nFetching \"CUSTOMER\ from database:\n\n")
cursor.execute("SELECT * FROM CUSTOMER")
for row in cursor:
    print(row)
    print("\n")