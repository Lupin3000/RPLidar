#!/usr/bin/env python3

import argparse
from datetime import datetime
from os import path

from rplidar import RPLidar

BAUDRATE: int = 115200
TIMEOUT: int = 1


def run():
    description = 'rplidar device info'
    epilog = 'The author assumes no liability for any damage caused by use.'
    parser = argparse.ArgumentParser(prog='./device_info.py', description=description, epilog=epilog)
    parser.add_argument('device', help="device path", type=str)
    args = parser.parse_args()
    dev_path = args.device

    if path.exists(dev_path):
        print('\n{:*^50s}'.format(" Lidar Status "))
        print('Found device : {0}'.format(dev_path))

        now = datetime.now()
        date_time = now.strftime("%d/%m/%Y %H:%M:%S")
        print('Date & Time  : {0}'.format(date_time))

        lidar = RPLidar(port=dev_path, baudrate=BAUDRATE, timeout=TIMEOUT)

        info = lidar.get_info()
        for key, value in info.items():
            print('{0:<13}: {1}'.format(key.capitalize(), str(value)))

        health = lidar.get_health()
        print('Health Status: {0[0]} - {0[1]}'.format(health))

        print('*' * 50)

        lidar.stop()
        lidar.stop_motor()
        lidar.disconnect()
    else:
        print('[Error] Could not found device: {0}'.format(dev_path))


if __name__ == '__main__':
    run()
