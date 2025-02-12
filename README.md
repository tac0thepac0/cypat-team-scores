# Welcome to the (Unofficial) Cyberpatriot Team Score Web-Viewer

The *Unofficial* Cyberpatriot Team Score Viewer creates a simple web interface designed to help teams and coaches visualize their team scores in real-time and as human-friendly as possible. Built using [Flask](https://flask.palletsprojects.com/en/stable/), the viewer was designed for coaches to host on their devices and allow teams to view their scores, provided that they are on the same network.

Although the [Cyberpatriot Scoreboard](https://scoreboard.uscyberpatriot.org/) has been updated in recent years, only one team can be displayed per tab. This viewer allows coaches to display the scores, play time, and penalties of multiple teams at the same time. 

## Installing and Running the Score Viewer

First, clone the repository:

```shell
git clone https://github.com/tac0thepac0/cypat-team-scores.git
```

Then install dependencies using pip:

```shell
cd cypat-team-scores
pip install -r requirements.txt
```

Finally, run the webserver:

```shell
python3 src/main.py
```

## Contributing

Look through existing [Issues](https://github.com/tac0thepac0/cypat-team-scores/issues) and [Pull Requests](https://github.com/tac0thepac0/cypat-team-scores/pulls) for any that you could help with. If you'd like to request a new feature or report a bug, please [create a new GitHub Issue](https://github.com/tac0thepac0/cypat-team-scores/issues).

## Disclamer

This software is not affiliated with neither the Air & Space Forces Association or the University of Texas at San Antonio. All scores displayed are unofficial and should be treated as such. The software does not provide predictions or assertions regarding advancement to subsequent rounds.

## License 

This software is open-source and licensed under the [GNU Public License](https://github.com/tac0thepac0/cypat-team-scores/blob/main/LICENSE).