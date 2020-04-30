import sqlite3,time

with sqlite3.connect("database.db") as db:
    cursor= db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS user(
userID INTEGER PRIMARY KEY,
usename VARCHAR(20) NOT NULL,
firstname VARCHAR(20) NOT NULL,
surname VARCHAR(20) NOT NULL,
password VARCHAR(20) NOT NULL);
''')    

#cursor.execute("""INSERT INTO user(usename,firstname,surname,password)
#VALUES("test_user","Bob","smith","MrBob")""")

db.commit()

cursor.execute("SELECT * FROM user")
print(cursor.fetchall())

