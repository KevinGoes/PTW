import psycopg2
import webbrowser

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


def get_navigation(adresses):
    link = 'http://www.google.es/maps/dir/Isotopenweg3/'
    for adress in adresses:
        adress = adress.replace(' ', '')
        link = link + adress + '/'
    link = link + 'Isotopenweg3/'
    return link


def get_places():
    c.execute("SELECT * FROM container")
    adresses = []
    for row in c.fetchall():
        if row[1] >= 80:
            adresses.append(row[2])
    return adresses


webbrowser.open(get_navigation(get_places()))
c.close()
conn.close()

