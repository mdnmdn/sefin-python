from psycopg2 import connect

# per evitare di mettere la connection string nel file
connection_string = os.environ.get('PG_CONNECTION_STRING')
# connection_string = 'postgres://pguser:xxxxxx@pg-hostname:54321/sakila'

conn = connect(connection_string)

cur = conn.cursor()


param = "family';  create table pippo(id int) -- "
#param = "Family"

sql = "select * from category where name = '%s' " % param
cur.execute(sql) ## NO MAI

print('sql:' , sql)
exit()



rows = cur.fetchall()

#print(rows)

for r in rows:
  print(r[0], r[1])

# informazioni sul risultato della query
#print(cur.description)

cur.close()

conn.close()
