@echo off 
echo   %1

echo %~dp0
cd %~dp0
echo %cd%
start python FBY-1FbyApk.py  %1
pause