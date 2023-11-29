import psycopg2 as psy
from opcua.opcua import OpcuaContainer as OpContainer
from opcua.opcuaReceiver import OpcuaReceiver as OpR
from opcua.opcuaTransmitter import OpcuaTransmitter as OpT

def fetchTable(cur, loc):
    cur.execute(f"SELECT * FROM {loc}")
    return cur.fetchall()

def getTableColumns(cur, table_name):
    cur.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table_name}'")
    return [column[0] for column in cur.fetchall()]

def main():
    conn = psy.connect(
        host = '118.138.154.172',
        user = 'kuka',
        password = 'kuka',
        database = 'NavBaseDB',
        port = 5432
        )

    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE table_catalog = 'NavBaseDB_Nav_KMR_200_iiwa_14_R820_1'
        """)
    rows = cur.fetchall()
    for row in rows:
        print(row)

    print(fetchTable(cur, 'localruntime.robotposition'))
    print(fetchTable(cur, 'config.robotinstance'))

    cols = getTableColumns(cur, 'localruntime.robotposition')
    print(cols)

    # for table_name in rows:
    #     schema = table_name[1]
    #     table_name = table_name[2]

    #     cur.execute(f"SELECT * FROM {schema}.{table_name}")
    #     row1 = cur.fetchall()
    #     print(f"Data from table {table_name}: {row1}")

    conn.commit()
    cur.close()
    conn.close()

if __name__ == '__main__':
    main()
