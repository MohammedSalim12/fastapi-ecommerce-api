import mysql.connector

dbcon = mysql.connector.connect(
    host="localhost",
    user="ecommerce",
    password="ecommerce",
    database="ecommerce"
)

mycursor = dbcon.cursor()
