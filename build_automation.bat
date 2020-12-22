
:: Windows build automation

:: Pass in projectName
@ECHO off
SET /p projectName="Enter projectName: "

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
FOR /F "delims=~" %%f in (requirements.txt) DO conda install --yes "%%f" || pip install "%%f"
@PAUSE && @CLS
CALL pip install .
@PAUSE && @CLS
CALL conda list
@PAUSE && @CLS

:: Test suite
CALL flake8 --statistics --exclude=notebooks,checkpoints
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

:: Launch applications
:: TBC - Data quality dashboard?
CALL jupyter lab
@PAUSE && @CLS

:: Remove virtual env when done
:: conda env remove -n %projectName%
:: CALL conda env list
:: @PAUSE && @CLS
