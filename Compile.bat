:: Title
ECHO OFF
TITLE Compile
CLS

:: Main
pyinstaller .\main.py --onefile --noconsole --name="Login"
PAUSE
