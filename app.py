from flask import Flask, jsonify, Response
from flask_cors import CORS
from db_pool import init_db, get_conn, release_conn


app = Flask(__name__)

# Enable CORS for local development & production
CORS(app, origins=["https://gregwdumont.github.io", "http://localhost:3000"])

@app.route("/api/projects")
def get_projects():
    conn = get_conn()
    cursor = conn.cursor()
    try:
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
    
    except Exception as e:
        print(f"Error fetching projects: {e}")
        return jsonify({'error': 'Internal server error'}), 500
    finally:
        cursor.close()
        release_conn(conn)

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
