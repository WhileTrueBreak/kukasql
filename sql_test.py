import psycopg2 as psy

conn = psy.connect(
    host = '127.0.0.1',
    user = 'kuka',
    password = 'kuka',
    database = 'NavBaseDB',
    port = 5432
    )

cur = conn.cursor()
cur.execute("""
    SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE table_catalog = 'NavBaseDB'
    """)
rows = cur.fetchall()
for row in rows:
    print(row)

for table_name in rows:
    schema = table_name[1]
    table_name = table_name[2]
    
    cur.execute(f"SELECT * FROM {schema}.{table_name}")
    row1 = cur.fetchall()
    print(f"Data from table {table_name}: {row1}")





conn.commit()
cur.close()
conn.close()