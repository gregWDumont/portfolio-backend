from fetch_svg_github_activity import fetch_svg_github_activity

dark_url = 'https://raw.githubusercontent.com/gregWDumont/gregWDumont/main/github-contribution-grid-snake-dark.svg'
light_url = 'https://raw.githubusercontent.com/gregWDumont/gregWDumont/main/github-contribution-grid-snake.svg'

fetch_svg_github_activity(dark_url, 'github-contribution-grid-snake-dark.svg')
fetch_svg_github_activity(light_url, 'github-contribution-grid-snake-light.svg')
