import psycopg2

try:
    conn = psycopg2.connect("dbname='lpdstrtn' "
                            "user='lpdstrtn' "
                            "host='dumbo.db.elephantsql.com' "
                            "password='OQBOtTdWyf5xbdDqwGFyi_T_rQ2KcjNw'")
    c = conn.cursor()
    # Print PostgreSQL version
    c.execute("SELECT version();")
    record = c.fetchone()
    print("You are connected to - ", record, "\n")

except:
    print("I am unable to connect to the database")


def read_from_db():
    c.execute("SELECT * FROM container")
    #data = c.fetchall()
    #print(data)
    for row in c.fetchall():
        print(row)


read_from_db()

c.close()
conn.close()