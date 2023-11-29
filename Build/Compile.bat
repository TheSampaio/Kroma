:: Title
ECHO OFF
TITLE Compile
CLS

:: Main
CD ../
SET /P NAME="Type the project's name: "
ECHO ===
pyinstaller Source/main.py --onedir --noconsole --noconfirm --name "%NAME%" --icon "../../../Data/Icon/icon-group-retiro.ico" --distpath "_Output/Bin/" --workpath "_Output/Obj/" --specpath "_Output/Obj/%NAME%"
ECHO ===
PAUSE
