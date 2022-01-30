# RPLidar A1M8

## Setup

**Clone Repository**

```shell
# clone repository
$ git clone https://github.com/Lupin3000/RPLidar.git

# change directory
$ cd RPLidar/
```

**Create virtualenv (_for Python 3.x_)**

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

> Depending on the rights settings, there may be problems with reading rights under Linux. Following quick and dirty solution can help.

```shell
# list device and permissions
$ ls -la /dev | grep ttyUSB

# change permissions
$ sudo chmod 0666 /dev/ttyUSB0
```
