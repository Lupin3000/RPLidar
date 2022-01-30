#!/usr/bin/env python3

import argparse
from os import path

from rplidar import RPLidar

BAUDRATE: int = 115200
TIMEOUT: int = 1


def run():
    description = 'rplidar measurement'
    epilog = 'The author assumes no liability for any damage caused by use.'
    parser = argparse.ArgumentParser(prog='./device_measurement.py', description=description, epilog=epilog)
    parser.add_argument('device', help="device path", type=str)
    args = parser.parse_args()
    dev_path = args.device

    if path.exists(dev_path):
        lidar = RPLidar(port=dev_path, baudrate=BAUDRATE, timeout=TIMEOUT)
        try:
            print('Print measurements - Press Crl+C to stop.')
            for val in lidar.iter_scans():
                print(val)
        except KeyboardInterrupt:
            lidar.disconnect()
    else:
        print('[Error] Could not found device: {0}'.format(dev_path))


if __name__ == '__main__':
    run()
