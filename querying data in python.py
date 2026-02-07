import mysql.connector

connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="abdullah1234",
    database="practice_db"
)
db=connection.cursor()
db.execute("""SELECT email FROM users WHERE date_of_birth = '2002-11-05'""")

for row in db:
    print(row)