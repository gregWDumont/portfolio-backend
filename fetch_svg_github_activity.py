from apscheduler.schedulers.background import BackgroundScheduler
from pathlib import Path
import requests
import os
import base64

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
        
        # Create 'static' folder if it doesn't exist
        Path("static").mkdir(exist_ok=True)
        
        with open(f'static/{file_name}', 'wb') as f:
            f.write(r.content)  # Use r.content to get binary content
    else:
        print(f"Failed to fetch SVG from {svg_url}: {r.status_code}, {r.text}")

if __name__ == "__main__":
    dark_url = 'https://raw.githubusercontent.com/gregWDumont/gregWDumont/main/github-contribution-grid-snake-dark.svg'
    light_url = 'https://raw.githubusercontent.com/gregWDumont/gregWDumont/main/github-contribution-grid-snake.svg'
    
    fetch_svg_github_activity(dark_url, 'github-contribution-grid-snake-dark.svg')
    fetch_svg_github_activity(light_url, 'github-contribution-grid-snake-light.svg')
