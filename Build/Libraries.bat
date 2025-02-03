ECHO OFF
TITLE Libraries
CLS

:: Main
ECHO Updating Pip...
python.exe -m pip install --upgrade pip
ECHO .

ECHO Installing or Updating PyInstaller...
pip install -U pyinstaller
ECHO .

PAUSE
