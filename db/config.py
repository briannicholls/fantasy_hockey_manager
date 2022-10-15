import psycopg2

# Connect to your postgres DB
# returns Connection if successful
conn = psycopg2.connect("dbname=fantasy_hockey_manager_bn user=postgres host='localhost' password=test1234" )

print("PostgreSQL server information")
print(conn.get_dsn_parameters(), "\n")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
cur.execute("""
CREATE TABLE IF NOT EXISTS players (
  id serial,
  external_id VARCHAR   UNIQUE NOT NULL,
  full_name   VARCHAR   NOT NULL
);
CREATE TABLE IF NOT EXISTS teams (
  id serial,
  external_id VARCHAR   UNIQUE NOT NULL,
  name        VARCHAR   NOT NULL
);

INSERT INTO "teams"   VALUES ( 1, 'XXX-XXX' , 'Test Team' ) ON CONFLICT DO NOTHING;
INSERT INTO "players" VALUES ( 2, 'XXX-XXX' , 'Test Player' ) ON CONFLICT DO NOTHING;

SELECT * FROM teams;
""")

# Retrieve query results
records = cur.fetchall()
