@echo off
echo Installing Python and required libraries for customCMD...

:: Check if Python is already installed
python --version 2>NUL
if %errorlevel%==0 (
    echo Python is already installed.
) else (
    :: Download and install Python 3.x
    echo Installing Python...
    :: Replace URL with the latest Python version
    powershell -Command "(New-Object Net.WebClient).DownloadFile('https://www.python.org/ftp/python/3.x.x/python-3.x.x.exe', 'python-installer.exe')"
    start /wait python-installer.exe /quiet
    del python-installer.exe
    echo Python installed successfully.
)

:: Install colorama library
echo Installing colorama library...
python -m pip install colorama

:: Clean up
echo Installation complete.
pause
