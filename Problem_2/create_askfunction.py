import sqlite3,time


def ask():
    ask=input("Doy You Want to Login or signUp?(L/S): ")
    if ask.upper() =="L":
        login()
    elif ask.upper() =="S":
        newuser()
    else:
        print("Try Again!!Please Enter Valid Alphabet.")
        
 
