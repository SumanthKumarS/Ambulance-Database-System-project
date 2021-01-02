import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="ambulance",
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS WORKER (id int(255),f_name VARCHAR(255),l_name VARCHAR(255),phone INT(10),email VARCHAR(255),dob DATE,gender VARCHAR(255),password VARCHAR(255))")

mycursor.execute("CREATE TABLE IF NOT EXISTS WORKER_MANAGE (worker_id int(255),name VARCHAR(255), phone INT(10),email VARCHAR(255),dob DATE,gender VARCHAR(255),address VARCHAR(255))")

mycursor.execute("CREATE TABLE IF NOT EXISTS USER (id int(255),f_name VARCHAR(255),l_name VARCHAR(255), phone INT(10),email VARCHAR(255),dob DATE,gender VARCHAR(255),password VARCHAR(255))")

mycursor.execute("CREATE TABLE IF NOT EXISTS USER_INFO (user_id int(255),name VARCHAR(255), phone INT(10),email VARCHAR(255),dob DATE,gender VARCHAR(255),address VARCHAR(255))")

mycursor.execute("CREATE TABLE IF NOT EXISTS REQUEST_ACCEPT (id VARCHAR(255),name VARCHAR(255),email VARCHAR(255),latitude VARCHAR(255),longitude VARCHAR(255),state VARCHAR(255),city VARCHAR(255),reqst_accept VARCHAR(255),date DATE,time TIME)")

mycursor.execute("CREATE TABLE IF NOT EXISTS REQUEST_ACCEPT (id VARCHAR(255),name VARCHAR(255),email VARCHAR(255),latitude VARCHAR(255),longitude VARCHAR(255),state VARCHAR(255),city VARCHAR(255),reqst_accept VARCHAR(255),date DATE,time TIME)")

mycursor.execute("CREATE TABLE IF NOT EXISTS REQUEST_DETAILS (id VARCHAR(255),name VARCHAR(255),email VARCHAR(255),latitude VARCHAR(255),longitude VARCHAR(255),state VARCHAR(255),city VARCHAR(255),reqst_accept VARCHAR(255),date DATE,time TIME)")

mycursor.execute("CREATE TABLE IF NOT EXISTS PATIENT_DETAILS (PNO INT(255),name VARCHAR(255),email VARCHAR(255),phone INT(10),address VARCHAR(255),place VARCHAR(255),date_time DATETIME)")

#mycursor.execute("SELECT * FROM worker")

#mycursor.execute("SELECT * FROM user")

mycursor.execute("SELECT * FROM worker_manage ")

print(mycursor.fetchall())

#print(r2.fetchall())

#mycursor.execute("SHOW DATABASES")

"""for x in mycursor:
  print(x)
"""
