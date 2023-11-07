@echo off

:: Create a virtual environment
python -m venv .venv

:: Activate the virtual environment (Windows)
call .venv\Scripts\activate

:: Install Python packages from requirements.txt
python -m pip install -r requirements.txt

