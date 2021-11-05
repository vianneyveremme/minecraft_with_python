@echo off

cd %~dp0/../../mcwpy/tests

FOR %%s in (
    datapack,
    pack_meta
) do (
    python3 -m unittest %%s
)

pause
EXIT /B %ERRORLEVEL%
