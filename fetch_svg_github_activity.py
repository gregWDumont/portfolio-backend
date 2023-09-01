from apscheduler.schedulers.background import BackgroundScheduler
import requests
import os
import base64

def fetch_svg_github_activity():
    token = os.environ.get('GITHUB_TOKEN')
    if not token:
        print("GitHub token not set")
        return

    headers = {'Authorization': f'token {token}'}
    svg_url = 'https://raw.githubusercontent.com/gregWDumont/gregWDumont/main/github-contribution-grid-snake-dark.svg'
    
    r = requests.get(svg_url, headers=headers)
    
    if r.status_code == 200:
        # Create static folder if it doesn't exist
        Path("static").mkdir(exist_ok=True)
        
        with open('static/github-contribution-grid-snake-dark.svg', 'wb') as f:
            f.write(r.content)  # Use r.content to get binary content
    else:
        print(f"Failed to fetch SVG: {r.status_code}, {r.text}")
