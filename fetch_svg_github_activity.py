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
    svg_url = 'https://github.com/gregWDumont/gregWDumont/blob/main/github-contribution-grid-snake-dark.svg'
    
    r = requests.get(svg_url, headers=headers)
    
    if r.status_code == 200:
        content = r.json().get('content')
        if content:
            decoded_content = base64.b64decode(content)
            with open('static/your-svg-file.svg', 'wb') as f:
                f.write(decoded_content)
    else:
        print(f"Failed to fetch SVG: {r.status_code}, {r.text}")
