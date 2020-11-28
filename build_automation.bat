
:: Windows build automation

:: Pass in projectName
@ECHO off
SET /p projectName="Enter projectName: "

:: Create virtual env
CALL conda create -n %projectName% python=3
CALL conda env list
@PAUSE

:: Switch to new virtual env
CALL conda activate %projectName%
CALL conda env list
@PAUSE

:: Install packages
:: conda list -e > requirements.txt
FOR /F "delims=~" %%f in (requirements.txt) DO conda install --yes "%%f" || pip install "%%f"
CALL pip install .
CALL conda list
@PAUSE

:: Test suite
@CLS
CALL flake8 --statistics
@PAUSE
@CLS
CALL pytest --verbose .
@PAUSE
@CLS
CALL coverage run --source src -m py.test
@PAUSE
@CLS
CALL coverage report --fail-under=100
@PAUSE

:: Data pipeline
@CLS
CALL python src/managers.py
@PAUSE
@CLS
CALL python src/stadiums.py
@PAUSE
@CLS
CALL python src/results.py
@PAUSE
@CLS
CALL python src/clubs.py
@PAUSE

:: Launch applications
:: TBC - Data quality dashboard?
@CLS
CALL jupyter lab
@PAUSE

:: Remove virtual env when done
:: conda env remove -n %projectName%
:: CALL conda env list
:: @PAUSE
