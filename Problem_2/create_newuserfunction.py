import sqlite3,time

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
