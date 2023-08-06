from flask import Flask, jsonify

app = Flask(__name__)

# Define a sample data to serve via the API
data = {
    "projects": [
        {"id": 1, "title": "Project 1", "description": "This is project 1."},
        {"id": 2, "title": "Project 2", "description": "This is project 2."},
    ]
}

@app.route("/api/projects")
def get_projects():
    return jsonify(data["projects"])

if __name__ == "__main__":
    app.run(debug=True)
