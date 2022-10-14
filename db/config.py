import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect("dbname=fantasy_hockey_manager user=postgres")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM teams")

# Retrieve query results
records = cur.fetchall()
