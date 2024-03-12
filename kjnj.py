import mysql.connector

# Replace placeholders with your actual connection details
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rootmysql",
    database=""
)
cursor = connection.cursor()

# Example: Select all rows from a table
query = "SELECT * FROM your_table;"
cursor.execute(query)

# Fetch all the rows
rows = cursor.fetchall()

# Display the results
for row in rows:
    print(row)

# Example: Insert a new record into a table
insert_query = "INSERT INTO your_table (column1, column2) VALUES (%s, %s);"
data_to_insert = ("value1", "value2")

cursor.execute(insert_query, data_to_insert)

# Commit the changes
connection.commit()

cursor.close()
connection.close()






