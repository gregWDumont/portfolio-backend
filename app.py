from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)

# Enable CORS for local development & production
CORS(app, origins=["https://gregwdumont.github.io", "http://localhost:3000"])

# Hard-code projects' content for now
data = {
    "projects": [
        {"id": 1, 
            "title": "Interactive Treemap Diagram", 
            "description": "This visualization features hierarchical data represented by color-coded rectangular tiles with variable fill colors, legends for category distinction, and tooltips that provide data insights upon mouse-over. The diagram fulfills specific user stories, creating elements with designated IDs, classes, and properties for an engaging data visualization experience.",
            "technologies": ["HTML", "CSS", "JavaScript", "D3"],
            "link": "https://codepen.io/reggr0y/pen/poOMZNd?editors=0110"
        },
        {
            "id": 2, "title": "Interactive Choropleth Map", 
            "description": "This visualization showcases counties color-coded with varying fill colors, representing educational data. The map adheres to a range of user stories, ensuring elements like titles, descriptions, legends, and tooltips with corresponding IDs and classes.",
            "technologies": ["HTML", "CSS", "JavaScript", "D3"],
            "link": "https://codepen.io/reggr0y/pen/QWVoBOR"
        },
        {
            "id": 3, 
            "title": "URL Shortener Microservice", 
            "description": "This microservice allows users to create short aliases for long URLs, making them easier to share and manage. The application adheres to a set of user stories, ensuring the implementation of features such as URL shortening, redirection, and analytics.",
            "technologies": ["Node.js", "Express.js", "MongoDB", "Mongoose", "HTML", "CSS", "JavaScript"],
            "link": "https://replit.com/@Reggr0y/boilerplate-project-urlshortener",
        },
        {
            "id": 4, 
            "title": "Pomodoro Clock", 
            "description": "This dynamic clock application aids in time management through the renowned Pomodoro Technique. It encompasses a range of user stories, ensuring the implementation of elements like session and break lengths, countdown display, control buttons, and audio cues. The clock adheres to a comprehensive set of functionalities, such as dynamic countdowns, pause-resume capabilities, and automatic transitions between sessions and breaks.",
            "technologies": ["HTML", "CSS", "JavaScript", "React"],
            "link": "https://codepen.io/reggr0y/pen/zYLaeMZ",
        },
        {
            "id": 5, 
            "title": "Probability Calculator", 
            "description": "Dive into the Probability Calculator project, utilizing an array of technologies including Python for scientific computing. This calculator empowers you to analyze probability distributions and simulate outcomes. The application effectively fulfills a set of user stories, ensuring functionalities like adding, removing, and computing probabilities for various events. Through Python's powerful libraries and tools, this Probability Calculator provides a versatile platform for probability analysis, enhancing your understanding of chance and randomness.",
            "technologies": ["Python"],
            "link": "https://replit.com/@Reggr0y/boilerplate-probability-calculator",
        },
    ]
}

@app.route("/api/projects")
def get_projects():
    return jsonify(data["projects"])
