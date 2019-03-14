
:: Generated requirements.txt using
:: conda list -e > requirements.txt

:: Pass in projectName
@ECHO off
SET /p projectName="Enter projectName: "

:: Create virtual env
conda create --name %projectName% python=3

:: Switch to new virtual env
activate %projectName%

:: One shot install - one fail, all fails
conda install --yes --file requirements.txt

:: Iterate over packages - Windows
FOR /F "delims=~" %%f in (requirements.txt) DO conda install --yes "%%f" || pip install "%%f"
:: Iterate over packages - Bash
:: while read requirement; do conda install --yes $requirement || pip install $requirement; done < requirements.txt

:: List installed packages
conda list

:: Remove virtual env when done
:: conda env remove -n %projectName%