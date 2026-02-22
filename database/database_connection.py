import mysql.connector

 #dbcon = mysql.connector.connect(
  #  host="localhost",
   # user="ecommerce",
    #password="ecommerce",
    #database="ecommerce"
#)

 # mycursor = dbcon.cursor()



import mysql.connector
import os

dbcon = mysql.connector.connect(
    host=os.getenv("MYSQLHOST"),
    user=os.getenv("MYSQLUSER"),
    password=os.getenv("MYSQLPASSWORD"),
    database=os.getenv("MYSQLDATABASE"),
    port=os.getenv("MYSQLPORT")
)


mycursor = dbcon.cursor(dictionary=True)
print("DB Connected Successfully")

def create_users_table():
    try:
        mycursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255),
                email VARCHAR(255) UNIQUE,
                password VARCHAR(255),
                phone VARCHAR(20)
            );
        """)
        dbcon.commit()
        print("Users table created successfully")
    except Exception as e:
        print("Error creating table:", e)
        
# استدعاء الدالة 
create_users_table()