[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
![GitHub repo size](https://img.shields.io/github/repo-size/deacona/the-ball-is-round)
![GitHub](https://img.shields.io/github/license/deacona/the-ball-is-round)
![GitHub last commit](https://img.shields.io/github/last-commit/deacona/the-ball-is-round)


the-ball-is-round
==============================

Having some fun with football stats and data science



## 1. Instructions

This project is written mostly in Python using the Miniconda distribution for Windows. To this end, I have a [script](build_automation.bat) to automate the build - setting up environment, running tests, processing data and launching applications.



## 2. Results

* World Cup 2018 predictions [notebook](notebooks/intl_01_world_cup_2018.ipynb) [report](reports/intl_01_world_cup_2018.md)
* Analysis of goals in European leagues [notebook](notebooks/club_01_goals_around_europe.ipynb) [report](reports/club_01_goals_around_europe.md)
* Predicting market value of Middlesbrough FC players [notebook](notebooks/boro_01_current_market_value.ipynb) [report](reports/boro_01_market_value.md)
* Shots analysis of Lionel Messi at Barcelona [notebook](notebooks/messi_01_finding_leo.ipynb) [report](reports/messi_01_finding_leo.md)
<!-- * [TBC] Which Boro players are most like Messi [notebook] [report]
* [TBC] World Cup 2022 predictions [notebook] [report]
* [TBC] Can Messi do it on a cold midweek night in Stoke [notebook] [report]
* [TBC] Boro player retention [notebook] [report] -->



## 3. Project Organisation

|Directory/File|Description|
|-----|-----|
|[app/](app/)|Web app for Dash dashboards, with [assets](app/assets/)|
|[data/](data/)|All the data, from the original [raw](data/raw/) data dump through to the final [processed](data/processed/) data|
|[models/](models/)|Trained and serialized models, model predictions, or model summaries|
|[notebooks/](notebooks/)|Jupyter notebooks. Naming convention is a project area, a number (for ordering), and a short description|
|[references/](references/)|Data dictionaries, manuals, and all other explanatory materials|
|[reports/](reports/)|Writen reports, with [figures](reports/figures)|
|[src/](src/)|Source code for use in this project|
|[tests/](tests/)|Test scripts|
|[build_automation.bat](build_automation.bat)|Script to automate enviroment setup, testing, data processing and application startups|
|[LICENSE](LICENSE)|Project license|
|[README.md](README.md)|This page :)|
|[requirements.txt](requirements.txt)|Standard Python dependencies file|
|[setup.py](setup.py)|Standard Python packaging script|



## 4. Licensing, Authors, Acknowledgements, etc.

Shoutouts to all the creators and maintainers of libraries that made this work possible.

Also, kudos to the data sources for publishing so much varied and interesting footdall data.

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>