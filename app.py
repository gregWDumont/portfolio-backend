from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)

# Enable CORS for local development - to be changed in production
CORS(app, origins="http://localhost:3000/portfolio-frontend/projects")

# Define a sample data to serve via the API
data = {
    "projects": [
        {"id": 1, "title": "Project 1", "description": "This is project 1."},
        {"id": 2, "title": "Project 2", "description": "This is project 2."},
        {"id": 3, "title": "Project 3", "description": "This is project 3."},
        {"id": 4, "title": "Project 4", "description": "This is project 4."},
        {"id": 5, "title": "Project 5", "description": "This is project 5."},
        {"id": 6, "title": "Project 6", "description": "This is project 6."},
    ]
}

@app.route("/api/projects")
def get_projects():
    return jsonify(data["projects"])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
