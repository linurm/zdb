@echo off
rem set GDB_DIR=C:\Users\zhj\AppData\Local\Android\sdk\ndk-bundle\prebuilt\android-arm\gdbserver
rem set ADB_DIR=g:\platform-tools
set GDB_DIR="g"
set ADB_DIR="a"
set GDBSERVER_DIR="g"
setlocal enabledelayedexpansion
for /f "tokens=1-3 delims==" %%i in (add.config) do (
set BL1=%%i
set BL2=%%j
set BL3=%%k
if "!BL1!"=="GDBSERVER_DIR"	(set GDBSERVER_DIR=!BL2!)
if "!BL1!"=="GDB_DIR"	(set GDB_DIR=!BL2!)
if "!BL1!"=="ADB_DIR"	(set ADB_DIR=!BL2!)
)
rem echo a1=!BL1!   a2=!BL2!   a3=!BL3!)

echo "GDBSERVER_DIR = %GDBSERVER_DIR%"
echo "GDB_DIR = %GDB_DIR%"
echo "ADB_DIR = %ADB_DIR%"


%ADB_DIR%\adb remount

%ADB_DIR%\adb push %GDBSERVER_DIR%\gdbserver /data
%ADB_DIR%\adb push %ADB_DIR%\add\android_server /data
%ADB_DIR%\adb shell chmod 777 /data/android_server
%ADB_DIR%\adb shell chmod 777 /data/gdbserver


rem call 2gdbpre.bat


cmd test.bat