
:: Windows build automation

:: Pass in projectName
@ECHO off
SET /p projectName="Enter projectName: "

:: Create virtual env
@REM CALL conda create -n %projectName% python=3
@REM CALL conda env list
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
@REM CALL conda list
@REM @PAUSE && @CLS

:: Test suite
CALL flake8 --max-complexity 10 --statistics --exclude=notebooks,checkpoints
@PAUSE && @CLS
CALL pytest --verbose .
@PAUSE && @CLS
@REM CALL coverage run --source src -m py.test
@REM CALL coverage report --fail-under=100
@REM @PAUSE && @CLS

:: Data pipeline
@REM CALL python src/managers.py
@REM @PAUSE && @CLS
@REM CALL python src/stadiums.py
@REM @PAUSE && @CLS
@REM CALL python src/results.py
@REM @PAUSE && @CLS
@REM CALL python src/clubs.py
@REM @PAUSE && @CLS
@REM CALL python src/events.py
@REM @PAUSE && @CLS
CALL python src/utilities.py
@PAUSE && @CLS

:: Run notebooks and export contents
jupyter nbconvert --to notebook --execute --inplace .\notebooks\*.ipynb
@PAUSE && @CLS
jupyter nbconvert --output-dir='.\notebooks\output' --to python .\notebooks\*.ipynb
@PAUSE && @CLS
jupyter nbconvert --no-input --output-dir='.\notebooks\output' --to markdown .\notebooks\*.ipynb
@PAUSE && @CLS

:: Launch applications
:: TBC - Data quality dashboard?
@REM CALL jupyter lab
@REM @PAUSE && @CLS

:: Remove virtual env when done
:: conda env remove -n %projectName%
:: CALL conda env list
:: @PAUSE && @CLS
