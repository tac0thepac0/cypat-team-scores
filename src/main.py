from requests import get
from flask import Flask, render_template

app = Flask(__name__)

# Team Number Format: xx-xxxx
data = {
        "<team-number>" : {},
        }

def get_scores(): 
    for team in data.keys():
        req = get("https://scoreboard.uscyberpatriot.org/api/team/scores.php", params={'team':team})
        data[team] = req.json()['data'][0]

@app.route("/")
def index():
    get_scores()
    return render_template('index.html', out=data)

if __name__ == '__main__':
    app.run()
