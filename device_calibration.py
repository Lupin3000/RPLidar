#!/usr/bin/env python3

import argparse
from os import path

from rplidar import RPLidar

BAUDRATE: int = 115200
TIMEOUT: int = 1


class PrintColor:
    YELLOW = '\033[1;33;48m'
    BLUE = '\033[1;34;48m'
    PURPLE = '\033[1;35;48m'
    END = '\033[1;37;0m'


def find_front(value):
    min_range = range(0, 10)
    max_range = range(350, 360)

    if value[2] == 0:
        print(PrintColor.YELLOW + "angle: {} distance: {} millimeter".format(value[2], value[3]) + PrintColor.END)

    if value[2] in min_range:
        print(PrintColor.BLUE + "angle: {} distance: {} millimeter".format(value[2], value[3]) + PrintColor.END)

    if value[2] in max_range:
        print(PrintColor.PURPLE + "angle: {} distance: {} millimeter".format(value[2], value[3]) + PrintColor.END)


def run():
    description = 'rplidar calibration from 350 to 360, 0, 0 to 10'
    epilog = 'The author assumes no liability for any damage caused by use.'
    parser = argparse.ArgumentParser(prog='./device_calibration.py', description=description, epilog=epilog)
    parser.add_argument('device', help="device path", type=str)
    args = parser.parse_args()
    dev_path = args.device

    if path.exists(dev_path):
        lidar = RPLidar(port=dev_path, baudrate=BAUDRATE, timeout=TIMEOUT)
        try:
            for val in lidar.iter_measures():
                if val[3] != 0:
                    find_front(val)
        except KeyboardInterrupt:
            lidar.stop()
            lidar.stop_motor()
            lidar.disconnect()
    else:
        print('[Error] Could not found device: {0}'.format(dev_path))


if __name__ == '__main__':
    run()
