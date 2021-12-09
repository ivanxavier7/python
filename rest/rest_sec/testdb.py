import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# Create table
create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

# Insert Data
user = (1, 'admin', 'asdf')
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

# Insert Multiple
users = [
    (2, 'Ivan', 'asdf'),
    (3, 'Francisco', 'asdf')
]
cursor.executemany(insert_query, users)

# Select
select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

connection.commit()
connection.close()