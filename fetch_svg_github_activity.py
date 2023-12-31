import requests
import os
from db_pool import init_db, get_conn, release_conn

def fetch_svg_github_activity(svg_url, file_name):
    """
    Fetches an SVG file from a specified GitHub URL and stores it in a PostgreSQL database.

    This function uses the requests library to make a GET request to the given SVG URL.
    If successful, it inserts the SVG data into the 'svgs' table in the database,
    updating the record if it already exists.

    Args:
        svg_url (str): URL of the SVG file on GitHub.
        file_name (str): Name under which the SVG will be stored in the database.

    The function requires a GitHub token set as an environment variable 'GITHUB_TOKEN' for authentication.
    """
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
    init_db()
    dark_url = 'https://raw.githubusercontent.com/gregWDumont/gregWDumont/main/github-contribution-grid-snake-dark.svg'
    light_url = 'https://raw.githubusercontent.com/gregWDumont/gregWDumont/main/github-contribution-grid-snake.svg'
    
    fetch_svg_github_activity(dark_url, 'github-contribution-grid-snake-dark.svg')
    fetch_svg_github_activity(light_url, 'github-contribution-grid-snake-light.svg')
