#!/usr/bin/python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  #passwd="yourpassword",
  database = "assignment"
)
mycursor = mydb.cursor()


f = open("seed_data.csv","r")
if f.mode == 'r':
    contents = f.readlines()
    for line in contents:
        if (line.find('email') != -1 ):
            continue
        element = line.split(',{')
        email = element[0]
        utm = '{0}{1}'.format("{",element[1])
        #print(email)
        #print(utm)
        sql = "INSERT INTO sample (email_id,utm_data) VALUES (%s,%s)"
        val = (email, utm)
        mycursor.execute(sql, val)
        mydb.commit()
f.close()
