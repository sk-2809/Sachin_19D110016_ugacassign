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


def login():
    while True:
        usename = input("Please Enter Your Username: ")
        password = input("Please Enter Your password: ")
        with sqlite3.connect("database.db") as db:
            cursor = db.cursor()
        find_user = ("SELECT * FROM user WHERE usename = ? AND password = ?")
        cursor.execute(find_user,[(usename),(password)])
        results = cursor.fetchall()

        if results:
            for i in results:
                print("Login Successfully!! Welcome " +i[2])
            break
             
        else:
            print("Usename and Password not recognised.")
            again = input("Do you want to try again?(y/n): ")
            if again.lower() == "n":
                print("Goodbye.Have a Good day!! :)")
                time.sleep(1)
                break


def newuser():
    found = 0
    while found ==0:
        usename = input("Please Enter Your Username: ")
        with sqlite3.connect("database.db") as db:
            cursor = db.cursor()
            finduser=("SELECT * FROM user WHERE usename = ?")
            cursor.execute(finduser,[(usename)])

        if cursor.fetchall():
             print("Usename Already Exist,Please try Other")
        else:
             found = 1

    firstname=input("Enter Your FirstName: ")
    surname=input("Enter Your SurName: ")
    password=input("Please Enter Your Password: ")
    password1=input("Please re-enter Your Password: ")
    while password!=password1:
        print("Your Password do not MATCH!!")
        password=input("Please Enter Your Password: ")
        password1=input("Please re-enter Your Password: ")

    insertdata = '''INSERT INTO user (usename,firstname,surname,password)
    VALUES(?,?,?,?)'''
    cursor.execute(insertdata,[(usename),(firstname),(surname),(password)])
    db.commit()
    print("SignUp Successfuly!!You can cheack Your Login.")

def ask():
    ask=input("Doy You Want to Login or signUp?(L/S): ")
    if ask.upper() =="L":
        login()
    elif ask.upper() =="S":
        newuser()
    else:
        print("Try Again!!Please Enter Valid Alphabet.")
        
        
    
ask()
