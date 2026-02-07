import mysql.connector

connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="abdullah1234",
    database="practice_db"
)
cursor=connection.cursor()
cursor.execute("CREATE DATABASE practice_db ")
