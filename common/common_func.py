import csv
import os


# 获取链接设备的系统版本号
def get_sys_version():
    results = os.popen("adb shell getprop ro.build.version.release")
    for result in results:
        print(result)
    return result


def get_devicesname():
    lnum = 0
    devicenames = os.popen("adb devices")
    for line in devicenames.readlines():
        lnum += 1
        if lnum == 2:
            device = line.split("device")[0].strip()
            print(device)
    return device

test = get_sys_version()
test2 = get_devicesname()