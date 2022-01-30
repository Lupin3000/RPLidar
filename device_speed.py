#!/usr/bin/env python3

import argparse
import time
from os import path

from rplidar import RPLidar

BAUDRATE: int = 115200
TIMEOUT: int = 1


def run():
    description = 'rplidar device speed'
    epilog = 'The author assumes no liability for any damage caused by use.'
    parser = argparse.ArgumentParser(prog='./device_speed.py', description=description, epilog=epilog)
    parser.add_argument('device', help="device path", type=str)
    args = parser.parse_args()
    dev_path = args.device

    if path.exists(dev_path):
        print('Found device : {0}'.format(dev_path))
        print('Print speed - Press Crl+C to stop.\n')
        print('*' * 50)

        lidar = RPLidar(port=dev_path, baudrate=BAUDRATE, timeout=TIMEOUT)
        old_t = None
        data = []

        try:
            for _ in lidar.iter_scans():
                now = time.time()

                if old_t is None:
                    old_t = now
                    continue

                delta = now - old_t

                print('{0:0.2f} Hz, {1:0.2f} RPM'.format(1 / delta, 60 / delta))

                data.append(delta)
                old_t = now
        except KeyboardInterrupt:
            lidar.stop()
            lidar.stop_motor()
            lidar.disconnect()

            delta = sum(data) / len(data)
            print('*' * 50)
            print('Mean: {0:0.2f} Hz, {1:0.2f} RPM'.format(1 / delta, 60 / delta))
    else:
        print('[Error] Could not found device: {0}'.format(dev_path))


if __name__ == '__main__':
    run()
