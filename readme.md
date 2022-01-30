# RPLidar A1M8

**:point_right: Very Important :point_left:**

You can adapt, improve and use the code for your projects as you wish. The author of this repository take no responsibility for your use or misuse or any damage on your devices!

## Information

The Python3 scripts for [RPLIDAR A1](https://www.slamtec.com/en/Lidar/A1) run on Linux, macOS and Windows. Latest rplidar documentation can be found [here](https://rplidar.readthedocs.io/en/latest/).

Examples:

- COM3 (_Windows_)
- /dev/ttyUSB0 (_Linux_)
- /dev/tty.usbserial-0001 (_macOS_)

## Setup

**Clone Repository**

```shell
# clone repository
$ git clone https://github.com/Lupin3000/RPLidar.git

# change directory
$ cd RPLidar/
```

**Create virtualenv (_for Python 3.x_)**

> The use of virtualenv is not mandatory but recommended.

```shell
# create virtualenv
$ virtualenv -p python3 venv

# activate virtualenv
$ . venv/bin/activate

# install packages
(venv) $ pip3 install -r requirements.txt 
```

## Execute Python scripts

**Display Device Information**

```shell
# show script help
(venv) $ python3 device_info.py -h

# display rplidar information and health status (macOS)
(venv) $ python3 device_info.py '/dev/tty.usbserial-0001'

# display rplidar information and health status (Linux)
(venv) $ python3 device_info.py '/dev/ttyUSB0'
```

**Display Measurements on Terminal**

```shell
# show script help
(venv) $ python3 device_measurement.py -h

# display rplidar measurements (macOS)
(venv) $ python3 device_measurement.py '/dev/tty.usbserial-0001'

# display rplidar measurements (Linux)
(venv) $ python3 device_measurement.py '/dev/ttyUSB0'
```

**Stop virtualenv**

```shell
# stop virtualenv
(venv) $ deactivate
```

## Error

**Linux**

> Root privilege is needed to access the ttyUSB device under Linux. Following quick and dirty solution can help or add KERNEL=="ttyUSB*", MODE="0666" to the configuration of udev, and reboot.

```shell
# list device and permissions
$ ls -la /dev | grep ttyUSB

# change permissions
$ sudo chmod 0666 /dev/ttyUSB0
```

**PyCharm**

> Some IDE like PyCharm show the problem "Unsatisfied package requirement inspection" because in file `requirements.txt` is written `rplidar-roboticia` and not `rplidar`.

Since RPLidar hardware is shipping with firmware >= 1.29 the usage of `$ pip3 install rplidar` will no more work! Please ignore such problem information.
