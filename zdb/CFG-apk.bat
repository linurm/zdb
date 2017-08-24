@echo off 
echo   %1

echo %~dp0
cd %~dp0
echo %cd%
python CFG-apk.py  %1