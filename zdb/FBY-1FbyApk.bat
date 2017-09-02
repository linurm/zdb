@echo off 
echo   %1

echo %~dp0
%~d0
cd %~p0
start python FBY-1FbyApk.py  %1
rem pause