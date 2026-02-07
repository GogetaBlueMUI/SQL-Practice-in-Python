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
table=PrettyTable()
db.execute("""SELECT MIN(salary) AS min_salary, MAX(salary) AS max_salary FROM users""")
db.execute("""SELECT gender, AVG(salary) AS avg_salary
FROM users
GROUP BY gender""")
db.execute("""SELECT name, gender,
       IF(gender = 'Female', 'Yes', 'No') AS is_female
FROM users;""")
table.field_names=[col[0] for col in db.description]

for row in db:
    table.add_row(row)
print(table)