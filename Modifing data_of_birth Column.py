import mysql.connector
import prettytable 
from prettytable import PrettyTable

connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="abdullah1234",
    database="practice_db"
)
db=connection.cursor()

db.execute("""ALTER TABLE Users MODIFY COLUMN date_of_birth  DATE NULL""")
db.execute("""
SELECT * FROM users 
WHERE name LIKE 'A%'
OR name LIKE '%a'
OR name LIKE '%li%'
""")
db.execute("""SELECT * FROM users ORDER BY date_of_birth ASC""")
db.execute("""SELECT * FROM users LIMIT 5""")
table=PrettyTable()
table.field_names=[col[0] for col in db.description]
for row in db:
    table.add_row(row)
print(table)