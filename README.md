the-ball-is-round
==============================

Having some fun with football stats and data science



## 1. Instructions

This project is written mostly in Python using the Anaconda distribution for Windows. To this end, I have a [script](build_automation.bat) to automate the build - setting up environment, running tests, processing data and launching applications. Before running this you'll need to add a config.ini file as per the [template](references/config.md).



## 2. Results

* World Cup 2018 predictions [notebook](notebooks/intl_01_world_cup_2018.ipynb) [report](reports/intl_01_world_cup_2018.md)
* Analysis of goals in European leagues [notebook](notebooks/club_01_goals_galore.ipynb) <!-- [report] -->
* Predicting market value of Middlesbrough FC players [notebook](notebooks/boro_01_current_market_value.ipynb) <!-- [report] -->
<!-- * [TBC] Analysis of Lionel Messi at Barcelona [notebook] [report]
* [TBC] Which Boro players are most like Messi [notebook] [report]
* [TBC] World Cup 2022 predictions [notebook] [report]
* [TBC] Can Messi do it on a cold midweek night in Stoke [notebook] [report]
* [TBC] Boro player retention [notebook] [report] -->



## 3. Project Organisation

|Directory/File|Description|
|-----|-----|
|[data/external/](data/external/)|Data from third party sources|
|[data/interim/](data/interim/)|Intermediate data that has been transformed|
|[data/processed/](data/processed/)|The final, canonical data sets for modeling|
|[data/raw/](data/raw/)|The original, immutable data dump|
|[models/](models/)|Trained and serialized models, model predictions, or model summaries|
|[notebooks/](notebooks/)|Jupyter notebooks. Naming convention is a project area, a number (for ordering), and a short description|
|[references/](references/)|Data dictionaries, manuals, and all other explanatory materials|
|[reports/](reports/)|Generated analysis as HTML, PDF, LaTeX, etc|
|[reports/figures/](reports/figures/)|Generated graphics and figures to be used in reporting|
|[src/](src/)|Source code for use in this project|
|[tests/](tests/)|Test scripts|
|[build_automation.bat](build_automation.bat)|Script to automate enviroment setup, testing, data processing and application startups|
|[LICENSE](LICENSE)|Project license|
|[README.md](README.md)|This page :)|
|[requirements.txt](requirements.txt)|Standard Python dependencies file|
|[setup.py](setup.py)|Standard Python packaging script|



## 4. Licensing, Authors, Acknowledgements, etc.

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>