""" CyberPatriot unofficial score display system """

from requests import get
from flask import Flask, render_template

app = Flask(__name__)

# Team Number Format: xx-xxxx
data = {
        "17-4007" : {},
        "17-4008" : {}
        }

def get_scores():
    """ Requests teams outlined in data and populates dictionary """
    # TODO: Rethink data handling logic
    for team in data:
        req = get(
            url="https://scoreboard.uscyberpatriot.org/api/team/scores.php",
            params={'team':team},
            timeout=3
        )
        data[team] = req.json()['data'][0]

def get_team_scores(team):
    """ Returns data for param team from dictionary data """
    # TODO: Re-evaluate logic for handling team scores
    if team in data:
        if not data[team]:
            get_scores()

        return data[team]
    else:
        return {}

def team_not_found(team):
    """ Returns content for case where a team is not found """
    # TODO: Create html file
    return f"Team {team} not found", 404

@app.route("/")
def index():
    """ Populate/Update dicitonary data and serve template with data """
    get_scores()
    return render_template('index.html', out=data)

@app.route("/<team>")
def team_scores(team=None):
    """ Serve template team.html with team specified in the URL """
    if team in data:
        return render_template('team.html', out=get_team_scores(team))
    else:
        return team_not_found(team)

if __name__ == '__main__':
    app.run()
