import sqlite3,time

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

