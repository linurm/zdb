
@echo off
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


%ADB_DIR%\adb shell rm -r system/app/GoogleEmail/GoogleEmail.apk
%ADB_DIR%\adb shell rm -r system/priv-app/RkExpe/RkExpe.apk
%ADB_DIR%\adb shell rm -r system/priv-app/MmsService/MmsService.apk
%ADB_DIR%\adb shell rm -r system/priv-app/Telecom/Telecom.apk
%ADB_DIR%\adb shell rm -r system/priv-app/TeleService/TeleService.apk
%ADB_DIR%\adb shell rm -r system/priv-app/TelephonyProvider/TelephonyProvider.apk
%ADB_DIR%\adb shell rm -r system/priv-app/VpnDialogs/VpnDialogs.apk
%ADB_DIR%\adb shell rm -r system/priv-app/StressTest/StressTest.apk
%ADB_DIR%\adb shell rm -r system/app/RKUpdateService/RKUpdateService.apk
%ADB_DIR%\adb shell rm -r system/app/PacProcessor/PacProcessor.apk
%ADB_DIR%\adb shell rm -r system/app/WAPPushManager/WAPPushManager.apk
%ADB_DIR%\adb shell rm -r system/app/BasicDreams/BasicDreams.apk
%ADB_DIR%\adb shell rm -r system/app/DeskClock/DeskClock.apk
%ADB_DIR%\adb shell rm -r system/app/PrintSpooler/PrintSpooler.apk
%ADB_DIR%\adb shell rm -r system/priv-app/CalendarProvider/CalendarProvider.apk
%ADB_DIR%\adb shell rm -r system/priv-app/projectX/projectX.apk

%ADB_DIR%\adb shell rm -r system/app/Camera2/Camera2.apk



%ADB_DIR%\adb shell
cmd
