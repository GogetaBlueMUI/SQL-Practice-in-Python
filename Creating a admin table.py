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
# db.execute("""CREATE TABLE admin_users (
# id INT PRIMARY KEY,
#  name VARCHAR(100),
#  email VARCHAR(100),
#  gender ENUM('Male', 'Female', 'Other'),
#  date_of_birth DATE,
#  salary INT
# )""")
# db.execute("""INSERT INTO admin_users (id, name, email, gender, date_of_birth, salary) VALUES
# (101, 'Anil Kumar', 'anil@example.com', 'Male', '1985-04-12', 60000),
# (102, 'Pooja Sharma', 'pooja@example.com', 'Female', '1992-09-20', 58000),
# (103, 'Rakesh Yadav', 'rakesh@example.com', 'Male', '1989-11-05', 54000),
# (104, 'Fatima Begum', 'fatima@example.com', 'Female', '1990-06-30', 62000)""")
db.execute("""Select name,email, 'Users' AS  role FROM users
UNION
SELECT name,email, 'Admin' AS role FROM admin_users""")
table.field_names=[col[0] for col in db.description]
for row in db:
    table.add_row(row)
print(table)
# connection.commit()