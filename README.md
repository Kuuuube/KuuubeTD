# KuuubeTD

Kuuube Tablet Driver, a driver for serial Wacom tablets.

### Proper documentation will be added soon.

`KT-0405-R/KT_0405_R_driver.py` has been tested only on KT-0405-R with rom version 1.3-2. To find your tablet's rom version run `tools/wacom_serial_tablet_diagnostics.py` (make sure to set your serial port path).

Install vmulti from `vmulti/vmulti_driver.zip`. (Extract and run `install_hiddriver.bat` as admin)

Change the serial port path in `KT-0405-R/constants.py` to what it should be for your setup. If you are unsure which path to use, run `tools/find_serial_port_paths.py`. You may have to guess between a few if there are multiple options.

For proper monitor mapping change the following variables in `KT-0405-R/constants.py` to what they should be for your setup: `ALL_MONITORS_RES_X`, `ALL_MONITORS_RES_Y`, `MAPPED_MONITOR_RES_X`, `MAPPED_MONITOR_RES_Y`, `OFFSET_X`, `OFFSET_Y`. Offsets are added from the top left corner.

You may also need to change `TABLET_MAX_X_POS` and `TABLET_MAX_Y_POS` if your tablet does not use the same resolution as mine.

You can define a custom tablet area by changing `TABLET_MAX_X_POS` and `TABLET_MAX_Y_POS` to be lower than the actual maxes. The tablet area can be positioned by changing `TABLET_OFFSET_X` and `TABLET_OFFSET_Y`. Offsets are added from the top left corner.

## KT-0405-R

### Settings applied by the driver:

Hex: `F233C900` Binary: `11110010001100111100100100000000`

`11` command set: WACOM IV

`11` baud rate: 19200

`00` parity: none

`1` data length: 8 bits

`0` stop bits: 1 stop bit

`00` CTS/DSR: none

`11` data transfer mode: stream

`0` output format: binary

`0` coordinate system: absolute

`11` transfer rate: maximum

`11` resolution: 1270 lpi

`0` origin location: upper left

`0` out-of-range data: no

`10` terminator: carriage return + line feed

`0` not used

`1` PnP: on

`0` pressure sensitivity: firm

`0` reading height: high

`0` multi device mode: disabled

`0` tilt mode: off

`0` MM command set: MM1201

`0` MM961 orientation: landscape

`0` BitPad II cursor data: 1234

`0` remote mode: off