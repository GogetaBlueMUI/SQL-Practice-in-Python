import mysql.connector

connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="abdullah1234",
    database="practice_db"
)
db=connection.cursor()

db.execute("DESCRIBE users")
for u in db:
    print(u)
db.execute("RENAME TABLE People to Users")