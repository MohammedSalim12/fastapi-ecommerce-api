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
    dbcon.commit()
    try:
        mycursor.execute("DROP TABLE IF EXISTS users;") 
        dbcon.commit()
        mycursor.execute("""
         
            CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(100) NOT NULL,
    user_password VARCHAR(255) NOT NULL,
    user_email VARCHAR(100) NOT NULL UNIQUE,
    user_phone VARCHAR(100) NOT NULL UNIQUE,
    user_verifycode INT NOT NULL,
    user_approve TINYINT NOT NULL DEFAULT 0,
    user_create TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
        """)
        dbcon.commit()
        print("Users table created successfully")
    except Exception as e:
        print("Error creating table:", e)
        
# استدعاء الدالة 
create_users_table()




