from psycopg2 import connect

# per evitare di mettere la connection string nel file
connection_string = os.environ.get('PG_CONNECTION_STRING')
# connection_string = 'postgres://pguser:xxxxxx@pg-hostname:54321/sakila'

conn = connect(connection_string)

cur = conn.cursor()


cat_id = 5

# cur.execute('select * from category where category_id = %s' % cat_id) ## NO MAI
sql = '  select * from category where category_id >= (%s) and  category_id <= (%s)'
cur.execute(sql, [ cat_id, cat_id + 5 ])

rows = cur.fetchall()

#print(rows)

for r in rows:
  print(r[0], r[1])

# informazioni sul risultato della query
#print(cur.description)

cur.close()

conn.close()
