from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)

# Enable CORS for local development & production
CORS(app, origins=["https://gregwdumont.github.io", "http://localhost:3000"])

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
