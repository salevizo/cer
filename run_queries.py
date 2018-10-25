#!/usr/bin/python

import psycopg2

conn = psycopg2.connect(database = "doi105281zenodo1167595", user = "postgres", password = "2", host = "127.0.0.1", port = "5432")
print "Opened database successfully"

cur = conn.cursor()

cur.execute("SELECT COUNT (DISTINCT shipname) FROM nari_ais_static");
rows = cur.fetchall()
for row in rows:
    print row;

print "Records created successfully";

conn.close()



######to run the file change the password of postgre user. Commands are listed below. I used as password:2
#sudo -u postgres psql postgres
#\password postgres
