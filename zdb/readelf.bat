@echo off 
echo   %1

echo %~dp0
%~d0
cd %~p0

python readelf.py

:1
set /p ip="   "
echo %ip%

python readelf.py  %ip%  %1

goto 1
pause