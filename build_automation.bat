
:: Windows build automation

:: Pass in projectName
@ECHO off
SET /p projectName="Enter projectName: "

:: Create virtual env
@REM CALL conda create -n %projectName% python=3
@REM @PAUSE && @CLS

:: Switch to new virtual env
CALL conda activate %projectName%
CALL conda env list
@PAUSE && @CLS

:: Install packages
:: conda list -e > requirements.txt
@REM FOR /F "delims=~" %%f in (requirements.txt) DO conda install --yes "%%f" || pip install "%%f"
@REM @PAUSE && @CLS
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
@REM CALL python src/managers.py
@REM @PAUSE && @CLS
@REM CALL python src/stadiums.py
@REM @PAUSE && @CLS
@REM CALL python src/results.py
@REM @PAUSE && @CLS
@REM CALL python src/clubs.py
@REM @PAUSE && @CLS
CALL python src/events.py
@PAUSE && @CLS

:: Launch applications
:: TBC - Data quality dashboard?
CALL jupyter lab
@PAUSE && @CLS

:: Remove virtual env when done
:: conda env remove -n %projectName%
:: CALL conda env list
:: @PAUSE && @CLS
