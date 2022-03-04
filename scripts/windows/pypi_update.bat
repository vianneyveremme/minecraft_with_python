@echo off
setlocal

cd %~dp0/../../

:: Run the setup verification script.
python3 verify_setup.py

:: Ask the user if the setup is correct.
:PROMPT
SET /P AREYOUSURE=Is the setup correct (Y/[N])?
IF /I "%AREYOUSURE%" NEQ "Y" GOTO CANCEL

:: Create the package.
python3 setup.py sdist

:PROMPT
SET /P AREYOUSURE=Do you want to upload the package to PyPI (Y/[N])?
IF /I "%AREYOUSURE%" NEQ "Y" GOTO CANCEL

:: Upload the package.
python3 -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

:PROMPT
SET /P AREYOUSURE=Do you want to remove the generated package (Y/[N])?
IF /I "%AREYOUSURE%" NEQ "Y" GOTO CANCEL

:: Remove the package.
RMDIR /S /Q dist
RMDIR /S /Q mcwpy.egg-info

:END
endlocal
pause
EXIT /B %ERRORLEVEL%

:CANCEL
echo "Cancelled"
goto END
EXIT /B 0
