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
    port=int(os.getenv("MYSQLPORT"))


)


mycursor = dbcon.cursor(dictionary=True)
print("DB Connected Successfully")

def create_users_table():
    mycursor.execute("DROP TABLE IF EXISTS users;")
    try:
        mycursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_name VARCHAR(255),
                user_email VARCHAR(255) UNIQUE,
                user_password VARCHAR(255),
                user_phone VARCHAR(20)
            );
        """)
        dbcon.commit()
        print("Users table created successfully")
    except Exception as e:
        print("Error creating table:", e)
        
# استدعاء الدالة 
create_users_table()