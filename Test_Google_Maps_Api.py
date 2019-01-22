import psycopg2

try:
    conn = psycopg2.connect("dbname='lpdstrtn' "
                            "user='lpdstrtn' "
                            "host='dumbo.db.elephantsql.com' "
                            "password='OQBOtTdWyf5xbdDqwGFyi_T_rQ2KcjNw'")
    c = conn.cursor()
    c.execute("SELECT version();")
    record = c.fetchone()
    print("You are connected to - ", record, "\n")

except:
    print("I am unable to connect to the database")


def get_navigation():
    c.execute("SELECT * FROM container")
    link = 'http://www.google.es/maps/dir/'
    for row in c.fetchall():
        adress = row[2]
        adress = adress.replace(' ', '')
        link = link + adress + '/'
    return link


print(get_navigation())
c.close()
conn.close()

