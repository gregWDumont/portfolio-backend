from flask import Flask, jsonify, Response
from flask_cors import CORS
import os
import psycopg2
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

app = Flask(__name__)

# Enable CORS for local development & production
CORS(app, origins=["https://gregwdumont.github.io", "http://localhost:3000"])

# Set up database connection
db_url = os.environ.get("DATABASE_URL")

print("Database URL:", db_url)

try:
    conn = psycopg2.connect(db_url)
    cursor = conn.cursor()
    print("Database connection successful")
except Exception as e:
    print("Database connection failed:", e)

@app.route("/api/projects")
def get_projects():
    cursor.execute("SELECT * FROM projects")
    projects_from_db = cursor.fetchall()

    projects = []
    for row in projects_from_db:
        projects.append({
            "id": row[0],
            "title": row[1],
            "description": row[2],
            "technologies": row[3],
            "link": row[4]
        })

    return jsonify(projects)

@app.route("/api/svgs/<svg_name>")
def get_svgs(svg_name):
    conn = get_conn()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT data FROM svgs WHERE name=%s", (svg_name,))
        svg_data = cursor.fetchone()
        if svg_data:
            return Response(svg_data[0], mimetype="image/svg+xml")
        else:
            return jsonify({'error': 'SVG not found'}), 404
    except Exception as e:
        print(f"Error fetching SVG: {e}")
        return jsonify({'error': 'Internal server error'}), 500
    finally:
        cursor.close()
        release_conn(conn)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
