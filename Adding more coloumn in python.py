import mysql.connector

connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="abdullah1234",
    database="practice_db"
)
db=connection.cursor()
db.execute("""ALTER TABLE Users ADD COLUMN Is_Active  BOOLEAN DEFAULT TRUE""")
db.execute("""ALTER TABLE Users DROP COLUMN Is_Active""")
