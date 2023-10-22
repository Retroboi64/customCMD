@echo off
chcp 65001 >nul
cls

:menu
echo [91m▄▄▄  [0m▄• ▄▌ ▐ ▄ 
echo [92m▀▄ █·[0m█▪██▌•█▌▐█
echo [93m▐▀▀▄ [0m█▌▐█▌▐█▐▐▌
echo [94m▐█•█▌[0m▐█▄█▌██▐█▌
echo [95m.▀  ▀ [0m▀▀▀ ▀▀ █▪

echo Please select the mode to run the customCMD script:
echo 1. Text-Based Mode
echo 2. GUI Mode
set /p mode="Enter the mode (1/2): "

if "%mode%"=="1" (
    echo Running in Text-Based Mode...
    python main.py
) else if "%mode%"=="2" (
    echo Running in GUI Mode...
    python gui.pyw
) else (
    echo Invalid input. Please enter 1 for Text-Based Mode or 2 for GUI Mode.
    goto menu
)

pause
