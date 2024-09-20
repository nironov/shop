import psycopg2


conn = psycopg2.connect('dbname=shopdb user=postgres password=123')
cur = conn.cursor()

