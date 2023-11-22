import pymysql

# Replace these values with your actual database connection details
host = '172.31.1.102'
user = 'kuka'
password = 'kuka'
database = 'NavBaseDB'
port = 5432  # Replace with the actual port number

# Create a connection to the database
connection = pymysql.connect(host=host, user=user, password=password, database=database, port=port)

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Now you can execute SQL queries using the 'cursor' object

# Example: Fetch all rows from a table named 'example_table'
cursor.execute('SELECT * FROM example_table')
rows = cursor.fetchall()

# Don't forget to close the cursor and connection when you're done
cursor.close()
connection.close()