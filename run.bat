@echo off
chcp 65001 >nul
cls

:menu
echo [91m▄▄▄  ▄• ▄▌ ▐ ▄ [0m
echo [92m▀▄ █·█▪██▌•█▌▐█[0m
echo [93m▐▀▀▄ █▌▐█▌▐█▐▐▌[0m
echo [94m▐█•█▌▐█▄█▌██▐█▌[0m
echo [95m.▀  ▀ ▀▀▀ ▀▀ █▪[0m
echo.
echo [91mWarning Run install bat if you have already installed it.[0m
echo.
echo Please select the mode to run the customCMD script:
echo 1. Text-Based Mode
echo 2. Credits
set /p mode="Enter the mode (1/2): "

if "%mode%"=="1" (
    echo Running in Text-Based Mode...
    python customCMD/main.py
if "%mode%"=="2" (
    echo Made by Retroboi64.
) else (
    echo Invalid input. Please enter 1 for Text-Based Mode
    goto menu
)

pause
