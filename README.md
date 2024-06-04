# multiwii-proxy-python

## Overview

A simple and user-friendly Python 3 module for controlling [_MultiWii_](https://github.com/multiwii/multiwii-firmware)-based drones using version 1.0 of the [_MultiWii Serial Protocol (MSP)_](http://www.multiwii.com/wiki/index.php?title=Multiwii_Serial_Protocol).

Formerly known as _WiiProxy_.

This module does **not** support MSP v2 or any of the newer versions.

## Documentation

The API documentation can be found on the [documentation site](https://bluday.github.io/multiwii-proxy-python/).

## Installation

Run either one of these commands to install the package:

```sh
python setup.py

pip install .
```

## Usage

```python
from serial import Serial

from multiwii import MultiWii

from multiwii.commands import MSP_IDENT

serial_port = Serial('/dev/ttyUSB0', baudrate=115200)

multiwii = MultiWii(serial_port)

ident = multiwii.get_data(MSP_IDENT)

print(repr(ident.multitype)) # <MultiWiiMultitype.QuadX: 3>
```

Other example usages can be found in the `examples` directory.

## Licensing

This project is licensed under the MIT license. See [LICENSE](https://github.com/BluDay/multiwii-proxy-python/blob/master/LICENSE) for more details.
