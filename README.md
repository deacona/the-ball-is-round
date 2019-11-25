the-ball-is-round
==============================

Having some fun with football stats and data science



## Dataset

This project comprises a wide variety of football data collected from various corners of the internet. Broadly it can be split into the following classes...
* Results - what happened in a match (goals, shots, cards, etc)
* Stadiums - where the teams play
* Managers - who was managing the team
* Clubs - team metrics (at the match level)
* Players - individual player metrics (currently at the season/competition level)
* Events [Coming soon!] - what exactly happened during a match and when did it happen
* International - some specific data collected on international competitions

My data pipeline ingests all of the raw data; cleans, standardises and combines it together to produce some  feature-rich data for analysis.



## Setup

The project is written (mostly) in Python (3.7). All the package dependencies are listed in `requirements.txt`. I am running 
the Anaconda distribution on Windows so have included `install_packages.bat` to create a virtual environment and install all of the packages.

_A simple workflow process_ [Coming soon!]



## World Cup predictions

In the Summer of 2018 my company held a World Cup prediction competition. I decided to tackle this scientifically!

__The challenge__
- Predict the scores for all group games
- 3 points for correct score, 2 points for correct goal difference, 1 point for correct result per game
- 50% of people will make it through to the next round (those with the highest points after the group games) where you will then go on to predict the scores for the remaining games

__My method__
1. Team ELO ratings were used to calculate a "Win expantancy" for each match
2. This was then weighted to give a likely result
3. To convert into a score further weights were applied based on whether the teams were involved in (relatively) high-scoring matches in qualifying
4. The predicted scores were then compared to historical data and the weights tuned against these historic expectations

The model can be [viewed here](
https://github.com/deacona/the-ball-is-round/blob/master/models/World%20cup%202018%20CALC.xlsx)
[Disclaimer - the model was built in Excel. I am planning to port it to Python before the next competition!]

__Results__

I finished in 2nd place, making it through each knockout round and to the final, only losing out there on goal difference! :-)

After all 64 matches here's how my model performed...

|Test|Count|% of total|
|-----|-----:|-----:|
|Correct result|34|53%|
|Correct goal difference|21|33%|
|Correct score|5|8%|
|Points scored|60|31%|
    
Generally I found that my model under-predicted the number of goals and wins.

||Goals per game|% games won|
|-----|-----:|-----:|
|Historic (1974-2014)|2.5|78%|
|Prediction (2018)|2.1|66%|
|Actual (2018)|2.6|78%|


Overall I was really pleased with how the model perfomed but there's still lots of room for improvement before next time!



Project Organization
------------

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    └── src                <- Source code for use in this project.


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>