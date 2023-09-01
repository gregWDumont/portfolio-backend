from flask import Flask, jsonify
from flask_cors import CORS
import os
import psycopg2
from apscheduler.schedulers.background import BackgroundScheduler
from fetch_svg_github_activity import fetch_svg_github_activity

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

scheduler = BackgroundScheduler()
scheduler.add_job(func=fetch_svg_github_activity, trigger="interval", seconds=3600)

if __name__ == "__main__":
    scheduler.start()
    app.run(debug=True)