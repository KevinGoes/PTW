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


def write_to_db(containernummer, volume):
    query = "UPDATE container SET volume =  %s WHERE containernummer = %s"
    data = (volume, containernummer)
    c.execute(query, data)
    conn.commit()
    #data = c.fetchall()
    #print(data)


write_to_db(101, 15)

c.close()
conn.close()
