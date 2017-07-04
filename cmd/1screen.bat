rem 
@echo off
adb remount
 
adb push add/build.prop /system
adb shell chmod 644 /system/build.prop

rem adb shell setprop persist.display.mode 0
call error.bat

call sleep3s.bat

pause 
rem call reboot.bat


