adb remount


adb shell setprop sys_graphic.cam_trace 0

adb shell dumpsys media.camera -v 0


call sleep3s.bat