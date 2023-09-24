import requests
import os
from psycopg2 import pool

DATABASE_POOL_SIZE = 5
database_pool = None

def init_db():
    global database_pool
    database_pool = pool.SimpleConnectionPool(1, DATABASE_POOL_SIZE, os.environ.get("DATABASE_URL"))

def get_conn():
    return database_pool.getconn()

def release_conn(conn):
    database_pool.putconn(conn)

def fetch_svg_github_activity(svg_url, file_name):
    print(f"Attempting to fetch SVG from {svg_url}...")
    
    token = os.environ.get('GITHUB_TOKEN')
    if not token:
        print("GitHub token not set")
        return

    headers = {'Authorization': f'token {token}'}
    r = requests.get(svg_url, headers=headers)
    
    if r.status_code == 200:
        print(f"Successfully fetched SVG from {svg_url}.")
        
        # Insert SVG into the PostgreSQL database using the pooled connection
        conn = get_conn()
        cursor = conn.cursor()
        try:
            print("Database connection successful")
            cursor.execute("INSERT INTO svgs (name, data) VALUES (%s, %s) ON CONFLICT (name) DO UPDATE SET data = EXCLUDED.data;", (file_name, r.content))
            conn.commit()
        except Exception as e:
            print(f"Database operation failed: {e}")
        finally:
            cursor.close()
            release_conn(conn)
    else:
        print(f"Failed to fetch SVG from {svg_url}: {r.status_code}, {r.text}")

if __name__ == "__main__":
    init_db()  # Initialize the database connection pool
    dark_url = 'https://raw.githubusercontent.com/gregWDumont/gregWDumont/main/github-contribution-grid-snake-dark.svg'
    light_url = 'https://raw.githubusercontent.com/gregWDumont/gregWDumont/main/github-contribution-grid-snake.svg'
    
    fetch_svg_github_activity(dark_url, 'github-contribution-grid-snake-dark.svg')
    fetch_svg_github_activity(light_url, 'github-contribution-grid-snake-light.svg')
