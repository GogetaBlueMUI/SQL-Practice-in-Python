import mysql.connector

connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="abdullah1234",
    database="practice_db"
)
db=connection.cursor()
db.execute("ALTER TABLE users MODIFY COLUMN name VARCHAR(150);")
db.execute("ALTER TABLE Users MODIFY COLUMN email VARCHAR(100) AFTER id")