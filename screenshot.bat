
set var=%time:~0,2%%time:~3,2%%time:~6,2%

adb shell /system/bin/screencap -p /sdcard/%var%.png

adb pull /sdcard/%var%.png  C:/Users/luo/Desktop/%var%.png

pause