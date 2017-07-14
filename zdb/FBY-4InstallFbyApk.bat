@echo off 
echo   %1

rem echo %~dp0
cd %~dp0
echo %cd%
start python FBY-4InstallFbyApk.py  %1
rem pause