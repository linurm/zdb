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



 
rem %ADB_DIR%\adb push ../add/gralloc.rk30board.so /system/lib/hw
call error.bat

rem %ADB_DIR%\adb push ../add/camera.rk30board.so /system/lib/hw
call error.bat

%ADB_DIR%\adb push ../add/audio.primary.rk30board.so /system/lib/hw
call error.bat

%ADB_DIR%\adb push ../add/audio.alsa_usb.rk30board.so /system/lib/hw
call error.bat
rem rk
rem %ADB_DIR%\adb push ../add/libcamera_client.so /system/lib
call error.bat

rem rk
rem %ADB_DIR%\adb push ../add/libcamera_metadata.so /system/lib
call error.bat

rem adb push libmedia.so /system/lib
rem call error.bat

rem %ADB_DIR%\adb push ../add/libcameraservice.so /system/lib
call error.bat


rem adb push add/libVR.so /system/lib
rem call error.bat
%ADB_DIR%\adb push ../add/libsurfaceflinger.so system/lib
call error.bat


%ADB_DIR%\adb push ../add/gralloc.default.so /system/lib/hw
call error.bat

%ADB_DIR%\adb push ../add/hwcomposer.rk30board.so /system/lib/hw
call error.bat

%ADB_DIR%\adb push ../add/hwcomposer.default.so /system/lib/hw
call error.bat

%ADB_DIR%\adb push ../add/libinputflinger.so /system/lib
call error.bat

rem adb push add/camera.slsiap.so /system/lib/hw
rem call error.bat

%ADB_DIR%\adb push ../add/libgui.so /system/lib
call error.bat

%ADB_DIR%\adb push ../add/libhardware.so /system/lib
call error.bat

%ADB_DIR%\adb push ../add/libandroid_runtime.so /system/lib
call error.bat


%ADB_DIR%\adb push ../add/libinputservice.so /system/lib
call error.bat

rem adb push recovery /system/bin
rem call error.bat

rem adb push build.prop /system
rem call error.bat

rem adb push libuart.so /system/lib
rem call error.bat

rem call jar.bat

rem call apk.bat

rem call sleep3s.bat
rem call sleep3s.bat
rem call sleep3s.bat
rem call sleep3s.bat

rem call reboot.bat


