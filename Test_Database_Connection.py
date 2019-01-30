import psycopg2

try:
    conn = psycopg2.connect("dbname='lpdstrtn' "
                            "user='lpdstrtn' "
                            "host='dumbo.db.elephantsql.com' "
                            "password='OQBOtTdWyf5xbdDqwGFyi_T_rQ2KcjNw'")
    c = conn.cursor()
    c.execute("SELECT version();")
    record = c.fetchone()
    print("Connection established \n\n")
    print("You are connected to -", record, "\n")

except:
    print("I am unable to connect to the database")