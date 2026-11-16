@echo off
setlocal

if /I "%~1"=="--help" goto help
if /I "%~1"=="--run" goto run
if /I "%~1"=="--fake" goto fake
if /I "%~1"=="--info" goto info

goto help
exit /b 0

:help
echo.
echo BlueScreen - Command Help
echo.
echo   BlueScreen          Show instructions
echo   BlueScreen --help   Show help
echo   BlueScreen --run    Run BSOD (Blue Screen) Script. This is a RISK to your files.
echo   BlueScreen --fake   Run fake BSOD simulation
echo   BlueScreen --info   Shows App info.
echo.
exit /b 0

:fake
py "%~dp0Scripts\FakeBlueScreen.py"
exit /b %errorlevel%
:info
echo.
echo BlueScreen CLI
echo Version: 1.0
echo Developer: Gavin Codework
echo Language: Batch + PowerShell + Python
echo Platform: Windows
echo.
echo BlueScreen is a command-line BSOD utility.
echo Includes real and simulated BSOD modes.
echo.
exit /b 0

:run
echo.
echo WARNING: You are about to run a BSOD (Blue Screen) RUNNER. This could remove any uncleared data or apps running.
echo This is free with changes and could break your Windows installation if you mess something up in this script.
echo RUN AT YOUR OWN RISK.
choice /C YN /M "Continue"
if errorlevel 2 exit /b 0

echo Starting BlueScreen
powershell -ExecutionPolicy Bypass -File "%~dp0Scripts\BlueScreen228406092.ps1"
echo Have fun 😈
exit /b 0
