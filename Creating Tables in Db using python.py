import mysql.connector

connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="abdullah1234",
    database="practice_db"
)
db=connection.cursor()
db.execute("""
CREATE TABLE users(
id int auto_increment PRIMARY KEY,
name varchar(100) NOT NULL, 
email varchar(100) UNIQUE NOT NULL, 
gender ENUM ('male','female','others'), 
date_of_birth DATE,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
""")

