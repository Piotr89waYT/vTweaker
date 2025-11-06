@echo off
echo Installing dependencies... (if already installed, this will be quick)
pip install -r requirements.txt

echo Starting vTweaker...
py main.py 
pause