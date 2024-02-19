import mysql.connector

database = mysql.connector.connect(
    host= 'localhost',
    user = 'root',
    password = 'your_password',
    auth_plugin='mysql_native_password',
)
#create cursor obj
cursorObject = database.cursor()

#create database
cursorObject.execute("CREATE DATABASE crm")
#cursorObject.execute("USE crm")
# cursorObject.execute("""CREATE TABLE RECORD(
#     first_name varchar(50) not null, last_name varchar(50) not null , email varchar(255) primary key not null ,address varchar(50)
#     not null , phone int(20) not null  )""")

#cursorObject.execute("drop table RECORD")
print("All done!")