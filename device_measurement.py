#!/usr/bin/env python3

import argparse
from datetime import datetime
from os import path

from rplidar import RPLidar

BAUDRATE: int = 115200
TIMEOUT: int = 1


def run():
    description = 'rplidar measurement'
    epilog = 'The author assumes no liability for any damage caused by use.'
    parser = argparse.ArgumentParser(prog='./device_measurement.py', description=description, epilog=epilog)
    parser.add_argument('device', help="device path", type=str)
    parser.add_argument("--raw", help="Show only measurement data", action="store_true")
    args = parser.parse_args()
    dev_path = args.device
    if args.raw:
        raw = True
    else:
        raw = False

    if path.exists(dev_path):
        lidar = RPLidar(port=dev_path, baudrate=BAUDRATE, timeout=TIMEOUT)
        try:
            if not raw:
                print('Print measurements - Press Crl+C to stop.')
                now = datetime.now()
                date_time = now.strftime("%d/%m/%Y %H:%M:%S")
                print('Date & Time  : {0}'.format(date_time))
            for val in lidar.iter_scans():
                print(val)
        except KeyboardInterrupt:
            lidar.stop()
            lidar.stop_motor()
            lidar.disconnect()
    else:
        print('[Error] Could not found device: {0}'.format(dev_path))


if __name__ == '__main__':
    run()
