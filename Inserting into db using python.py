import mysql.connector

connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="abdullah1234",
    database="practice_db"
)
db=connection.cursor()
db.execute("""INSERT INTO Users VALUES
(DEFAULT,'muhammadabdullah090809@gmail.com','Abdullah','male','2002-11-05',DEFAULT)""")
connection.commit()
db.execute("SELECT * FROM Users")
for c in db:
    print(*c)