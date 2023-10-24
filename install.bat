@echo off
echo Installing Python and required libraries for customCMD...


python --version 2>NUL
if %errorlevel%==0 (
    echo Python is already installed.
) else (
    :: Download and install Python 3.11
    echo Installing Python...
    
    powershell -Command "(New-Object Net.WebClient).DownloadFile('https://www.python.org/ftp/python/3.11.6/python-3.11.6.exe', 'python-installer.exe')"
    start /wait python-installer.exe /quiet
    del python-installer.exe
    echo Python installed successfully.
)


echo Installing all librarys...
python -m pip install -r requirements.txt




echo Installation complete.
pause
