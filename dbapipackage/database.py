import sqlite3

# Connecting to sqlite
# connection object
conn = sqlite3.connect('database.db')
print ("Opened database successfully")

# cursor object
cursor_obj = conn.cursor()
 
# Drop the GEEK table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS users")

# Creating table  ---- with multiple inverted commas, we can write the query in mutliple lines.
query = """ CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(25) NOT NULL,
            age INT            
        ); """

cursor_obj.execute(query) #'CREATE TABLE users (id INT AUTOINCREMENT , name TEXT, age INT)')
print ("Table created successfully")

# Close the connection
conn.close()

