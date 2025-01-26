from requests import get
from flask import Flask, render_template

app = Flask(__name__)

# Team Number Format: xx-xxxx
data = {
        "17-4007" : {},
        "17-4008" : {}
        }

def get_scores():
    for team in data.keys():
        req = get("https://scoreboard.uscyberpatriot.org/api/team/scores.php", params={'team':team})
        data[team] = req.json()['data'][0]

def get_team_scores(team):
    if team in data:
        if not data[team]:
            get_scores()

        return data[team]
    else:
        return {}

@app.route("/")
def index():
    get_scores()
    return render_template('index.html', out=data)

@app.route("/<team>")
def team_scores(team=None):
    return render_template('team.html', out=get_team_scores(team))

if __name__ == '__main__':
    app.run()
