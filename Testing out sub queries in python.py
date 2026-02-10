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
# db.execute("""ALTER TABLE users
# ADD COLUMN referred_by_id INT;
# """)
# db.execute("""UPDATE users SET referred_by_id =1 WHERE id IN (1,2,3,4,5)""")
# db.execute("""UPDATE users SET referred_by_id =2 WHERE id IN (20)""")
db.execute("""SELECT id, name, referred_by_id FROM users WHERE referred_by_id IN (
SELECT  id FROM users WHERE salary > 50000) """)
table.field_names=[col[0] for col in db.description]
for row in db:
    table.add_row(row)
print(row)