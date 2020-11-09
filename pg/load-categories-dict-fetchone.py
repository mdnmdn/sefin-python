from psycopg2 import connect, extras

# per evitare di mettere la connection string nel file
connection_string = os.environ.get('PG_CONNECTION_STRING')
# connection_string = 'postgres://pguser:xxxxxx@pg-hostname:54321/sakila'

conn = connect(connection_string)

# configuro il cursore per restituire i risultati con chiave il nome della colonna
with conn.cursor(cursor_factory = extras.DictCursor) as cur:
  sql = 'select * from category'
  cur.execute(sql, [])

  row = cur.fetchone()
  while row != None:
    print(row['category_id'], row['name'])
    row = cur.fetchone()


# informazioni sul risultato della query
#print(cur.description)

conn.close()
