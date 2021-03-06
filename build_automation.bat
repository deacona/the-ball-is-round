
:: Windows build automation

:: Pass in environment vars
@ECHO off
SET /p projectName="Enter Conda env name: "
SET /p projectPath="Enter Project path: "
@REM SET projectName=
@REM SET projectPath=

:: Remove virtual env when done
@REM CALL conda deactivate
@REM CALL conda env remove -n %projectName%
@REM CALL conda env list
@REM @PAUSE && @CLS

:: Create virtual env
CALL conda create -n %projectName% python=3
CALL conda env list
@PAUSE && @CLS

:: Switch to new virtual env
CALL conda activate %projectName%
CALL conda env list
@PAUSE && @CLS

:: Install packages
:: conda list -e > requirements.txt
:: FOR /F "delims=~" %%f in (requirements.txt) DO conda install --yes "%%f" || pip install "%%f"
CALL pip install -r requirements.txt
CALL conda install basemap
@PAUSE && @CLS
CALL isort --profile black --skip notebooks .
@PAUSE && @CLS
CALL black . --exclude notebooks
@PAUSE && @CLS
CALL pip install .
@PAUSE && @CLS
@REM CALL conda list
@REM @PAUSE && @CLS

:: Test suite (S101 = Use of assert)
CALL flake8 --max-complexity 10 --max-line-length 99 --statistics --ignore=S101 --exclude notebooks,*/.ipynb_checkpoints/*
@PAUSE && @CLS
@REM CALL bandit -r .
@REM @PAUSE && @CLS
CALL pylint --disable=all --enable=duplicate-code ./src/
@PAUSE && @CLS
CALL pytest --verbose .
@PAUSE && @CLS
CALL coverage run --source src -m py.test
CALL coverage report --fail-under=100
@PAUSE && @CLS

:: Data pipeline
CALL python src/managers.py
@PAUSE && @CLS
CALL python src/stadiums.py
@PAUSE && @CLS
CALL python src/results.py
@PAUSE && @CLS
CALL python src/clubs.py
@PAUSE && @CLS
CALL python src/players.py
@PAUSE && @CLS
CALL python src/events.py
@PAUSE && @CLS
CALL python src/nations.py
@PAUSE && @CLS

:: Run data quality tests and launch Dash data quality dashboard
CALL python src/quality.py
@PAUSE && @CLS
START /min python app/app.py
START "" "http://localhost:8050/"

:: Clear previous exports, run notebooks, export contents and launch Jupyter for analysis
CALL python src/utilities.py
@PAUSE && @CLS
jupyter nbconvert --to notebook --execute --inplace .\notebooks\*.ipynb
@PAUSE && @CLS
jupyter nbconvert --output-dir='.\notebooks\output' --to python .\notebooks\*.ipynb
@PAUSE && @CLS
jupyter nbconvert --no-input --output-dir='.\notebooks\output' --to markdown .\notebooks\*.ipynb
@PAUSE && @CLS
@REM START /min jupyter lab
START /min jupyter lab --no-browser
@PAUSE && @CLS