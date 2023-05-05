# KuuubeTD

Kuuube Tablet Driver, a driver for old graphics tablets which use a serial port.

## Usage

Find your tablet's ROM version then use the applicable version. To find your tablet's ROM version, follow [Finding ROM Version](./docs/finding_rom_version.md).

### [Wacom IVe 1.4](./docs/wacom_ive_1_4.md)

### [Wacom IV 1.2-1.4](./docs/wacom_iv_1_2_to_1_4.md)

### [Wacom IV 1.0-1.1](./docs/wacom_iv_1_0_to_1_1.md)

### [Wacom II-S](./docs/wacom_ii_s.md)

### [Wacom II](./docs/wacom_ii.md)

## Dependencies

Python 3: [Download link](https://www.python.org/downloads/)

Python `pyserial` and `pywinusb` modules: To install them, enter the following command in cmd or a terminal:

```
pip install pyserial
pip install pywinusb
```

## Features

- Support for various old tablets that use a serial port and no longer have any official support.

- Full windows ink support for pen pressure, eraser detection, and barrel button detection.

- Custom tablet and monitor area mappings.

## FAQ

[FAQ](./docs/faq.md)

## Supported Tablets

[Supported Tablets List](./docs/supported_tablets.md)

## Issues and Troubleshooting

If you have any issues regarding tablet support or driver function, join the [Discord Server](https://discord.gg/T5vEAh4ruF) for help. This includes requests for supporting more tablets.

I would also appreciate it if you let me know of any tablets currently listed as untested that you can verify work with the driver.

If you would rather not join the discord server, you may create an issue on this repo. However, it is usually much faster to work over discord.

## Contributing

Pull requests for any improvements are likely to be accepted. 

If you are unsure whether a feature is reasonable to add, make an issue or ask in the [Discord Server](https://discord.gg/T5vEAh4ruF) first. 

There are no strict rules on what is acceptable, but try to follow the general style of the existing code and commit names.