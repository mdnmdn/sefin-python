from psycopg2 import connect, extras

import psycopg2

import psycopg2 as pgdriver # alias

from mysqlx.connection import connect

# from <package/modulo>.<sottomodulo> import <oggetto da importare> as <eventuale alias>

from mysqlx import connection as mysqldriver


# per evitare di mettere la connection string nel file
connection_string = os.environ.get('PG_CONNECTION_STRING')
# connection_string = 'postgres://pguser:xxxxxx@pg-hostname:54321/sakila'

conn = psycopg2.connect(connection_string)
conn2 = pgdriver.connect(connection_string)
conn3 = mysqldriver.connect('')

# configuro il cursore per restituire i risultati con chiave il nome della colonna
with conn.cursor(cursor_factory = psycopg2.extras.DictCursor) as cur:
  sql = 'select * from category'
  cur.execute(sql, [])

  rows = cur.fetchall()

#print(rows)

for r in rows:  
  print(r['category_id'], r['name'])

# informazioni sul risultato della query
#print(cur.description)

conn.close()
