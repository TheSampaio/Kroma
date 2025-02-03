@ECHO OFF
TITLE Compile
CLS

:: Navigate to the parent directory
CD ../

:: Get the project name from user input
SET /P NAME="Enter the project name: "

:: Separator for readability
ECHO.
ECHO ==================================
ECHO      Compiling Project: %NAME%
ECHO ==================================
ECHO.

:: Run PyInstaller with the specified settings
pyinstaller Source/main.py ^
    --onedir ^
    --noconsole ^
    --noconfirm ^
    --name "%NAME%" ^
    --icon "../../../_internal/_data/icon-kroma.ico" ^
    --distpath "_output/bin/" ^
    --workpath "_output/obj/" ^
    --specpath "_output/obj/%NAME%"

:: Completion message
ECHO.
ECHO ==============================
ECHO      Compilation Finished
ECHO ==============================
ECHO.

PAUSE
