
:: Windows build automation

:: Pass in environment vars
@ECHO off
SET /p projectName="Enter Conda env name: "
SET /p projectPath="Enter Project path: "

:: Remove virtual env when done
@REM CALL conda deactivate
@REM CALL conda env remove -n %projectName%
@REM CALL conda env list
@REM @PAUSE && @CLS

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
:: FOR /F "delims=~" %%f in (requirements.txt) DO conda install --yes "%%f" || pip install "%%f"
@REM CALL pip install -r requirements.txt
@REM CALL conda install basemap
@REM @PAUSE && @CLS
CALL isort --profile black --skip notebooks .
@PAUSE && @CLS
CALL black . --exclude notebooks
@PAUSE && @CLS
CALL pip install .
@PAUSE && @CLS
@REM CALL conda list
@REM @PAUSE && @CLS

:: Test suite
CALL flake8 --max-complexity 10 --statistics --exclude notebooks,*/.ipynb_checkpoints/*
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
@REM CALL python src/utilities.py
@REM @PAUSE && @CLS

:: Run notebooks and export contents
@REM jupyter nbconvert --to notebook --execute --inplace .\notebooks\*.ipynb
@REM @PAUSE && @CLS
@REM jupyter nbconvert --output-dir='.\notebooks\output' --to python .\notebooks\*.ipynb
@REM @PAUSE && @CLS
@REM jupyter nbconvert --no-input --output-dir='.\notebooks\output' --to markdown .\notebooks\*.ipynb
@REM @PAUSE && @CLS

:: Launch applications
:: TBC - Data quality dashboard?
@REM CALL jupyter lab
@REM @PAUSE && @CLS