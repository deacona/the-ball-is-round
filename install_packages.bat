
:: Generated requirements.txt using
:: conda list -e > requirements.txt

:: Pass in projectName
@ECHO off
SET /p projectName="Enter projectName: "

:: Create virtual env
CALL conda create -n %projectName% python=3
CALL conda env list

:: Switch to new virtual env
CALL conda activate %projectName%
CALL conda env list

:: Install libraries
@REM pip install -r requirements.txt
FOR /F "delims=~" %%f in (requirements.txt) DO conda install --yes "%%f" || pip install "%%f"
CALL pip install .
CALL conda list

:: Test suite
CALL flake8 --statistics
CALL pytest --verbose .
CALL coverage run --source src -m py.test
CALL coverage report --fail-under=100

:: Load data
CALL python managers.py
CALL python stadiums.py
CALL python results.py
CALL python clubs.py

:: Launch applications
REM Data quality dashboard?
CALL jupyter lab

:: Remove virtual env when done
:: conda env remove -n %projectName%

@pause