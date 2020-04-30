# Sachin_19D110016_ugacassign

## Description For Each Problem are given below:<br>
* Problem 0: In this problem I have to create a XAMPP local server in my computer,So I have downloaded the XAMPP setup from link (https://www.apachefriends.org/index.html). After that I have installed it to my computer and created a local server in my computer.Creating local server using XAMPP helps me to check the php files made for Problem 1,And creating local server also help me in creating database in problem 4. <br><br>


* Problem 1: In this problem I have to make user-login page and user-registration page using using HTML and CSS.And also to make the page functional using PHP and SQL that can display the username of the user after Successful login.And also to give a logout button after getting login to your page.
   
   I have created a UserLogin.php which contain all the componenet of fist page which is divided into two part one is SignUp and other      one is Login.In that page you have to signup first in order to make yourself eligible for a successful login.When you sign up by giving your choice of username and password.Then that data will get stored in userlogin.db(database file).
   
   when you want to login then it is cheacked whether you have previously sign up or not.If you have previously signup then your username and password will be there in database file and then you can login to your page.
   
   When you get login,a new page will appear which contain a hi msg to you along with your username.Just below that line,there is a logout button.Logout button will make you to get your account logout from that page.And again same UserLogin page will apper.
    
    In this Problem I have used bootstap4.4(https://getbootstrap.com/docs/4.4/getting-started/introduction/).I don't have used online link.I have downloded the file of css from bootstrap and linked it to UserLogin.php file.In this Problem I have used the backgroung image whose link is (https://images.unsplash.com/photo-1501785888041-af3ef285b470?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1500&q=80).I have also uploded the image on Problem_1 folder of this repository  <br>


* Problem 2 : In this problem I have to write a python script which takes username and password of a user as
terminal input and shows a login success or failure message.

   In this problem I have used sqlite3 library(https://www.sqlitetutorial.net/sqlite-python/) of python which helps me create a database.I have created database.db as my database which I have uploded in Problem_2 folder of this directory.I have made a Problem_2.py file which include all the function that i have created indivisually to make this project complete.

   I have made a create_database.py file which contains the code of creating the database. <br>
   I have made a create_loginfunction.py file which contain definition of login function.Login function helps to get login successfully,if you have already sign up.
   I have made create_newuserfunction.py file which contain newuser function that will make a new usser to add data to the database,to get login to his data.
   I have made a create_askfunction.py file which contain ask function that is made to work whole things successfully by asking the user whether he/she want to get login or to sign up themselves. 




* Problem 3(This is bonus question.):In this problem I have to make a python script to read the data of JSON file(https://gymkhana.iitb.ac.in/~ugacademics/model.json) and get stored in a database of local server in myphpadmin as a table.

     I have made a json_to_database.py file which contains the code of making json file read,create a table in database of local host,and make it to get store inside the database of local server(created in problem 0). <br>


