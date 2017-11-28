@echo off 
echo   %1

echo %~dp0
%~d0
cd %~p0

start python FBY-3RebuildApk.py %1
rem ".apk"


pause