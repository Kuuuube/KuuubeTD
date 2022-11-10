# Wacom IV 1.0-1.1:

## Usage

- Install vmulti from `vmulti/vmulti_driver.zip`. (Extract and run `install_hiddriver.bat` as admin.)

- Change `SERIAL_PORT_PATH` in `KuuubeTD/user_constants.py` to the path the tablet is connected to.

    If you are unsure which path to use, run `tools/find_serial_port_paths.py`. (You may have to guess between a few if there are multiple options.)

- Run `KuuubeTD/wacom_iv_1_0_to_1_1_driver.py` (Coming Soon)

    To find your tablet's rom version run `tools/wacom_serial_tablet_diagnostics.py`. (Make sure to set your serial port path.)

- For proper monitor mapping, change the following variables in `KuuubeTD/user_constants.py` to the correct values for your setup: 

    `ALL_MONITORS_RES_X`: This is the X axis resolution of all your monitors combined. 
    
    For example, two 1920 x 1080 monitors positioned side by side have an `ALL_MONITORS_RES_X` of 3840, and two 1920 x 1080 monitors positioned up and down have an `ALL_MONITORS_RES_X` of 1080.

    `ALL_MONITORS_RES_Y`: This is the Y axis resolution of all your monitors combined. 
    
    For example, two 1920 x 1080 monitors positioned side by side have an `ALL_MONITORS_RES_Y` of 1080, and two 1920 x 1080 monitors positioned up and down have an `ALL_MONITORS_RES_Y` of 2160.

    `MAPPED_MONITOR_RES_X`: This is the X axis resolution of the monitor mapping to apply. 
    
    For example, to map to a 1920 x 1080 monitor, the `MAPPED_MONITOR_RES_X` will be 1920 regardless of how many monitors you have.

    `MAPPED_MONITOR_RES_Y`: This is the Y axis resolution of the monitor mapping to apply. 
    
    For example, to map to a 1920 x 1080 monitor, the `MAPPED_MONITOR_RES_Y` will be 1080 regardless of how many monitors you have.
    
    `MONITOR_OFFSET_X`: This is the X axis offset to apply to `MAPPED_MONITOR_RES_X`. (Offsets are added from the top left corner.)

    For example, on a setup with two 1920 x 1080 monitors side by side, to map to the right monitor, `MONITOR_OFFSET_X` will be 1920, and to map to the left monitor, `MONITOR_OFFSET_X` will be 0.
    
    `MONITOR_OFFSET_Y`: This is the Y axis offset to apply to `MAPPED_MONITOR_RES_Y`. (Offsets are added from the top left corner.)

    For example, on a setup with two 1920 x 1080 monitors up and down, to map to the bottom monitor, `MONITOR_OFFSET_Y` will be 1080, and to map to the top monitor, `MONITOR_OFFSET_Y` will be 0.
    
- Optionally, to use a custom tablet area instead of full area, change the following variables in `KuuubeTD/user_constants.py` to the desired values:

    `TABLET_MAX_X_POS`: The tablet area width in tablet coordinates to use for the size of the tablet area.

    `TABLET_MAX_Y_POS`: The tablet area height in tablet coordinates to use for the size of the tablet area.

    `TABLET_OFFSET_X`: The X axis offset to apply to `TABLET_MAX_X_POS` in tablet coordinates to change the position of the tablet area. (Offsets are added from the top left corner.)

    `TABLET_OFFSET_Y`: The Y axis offset to apply to `TABLET_MAX_Y_POS` in tablet coordinates to change the position of the tablet area. (Offsets are added from the top left corner.)

## Notes

### Settings Command:

```
~*F233C900,000,00,1270,1270
```

### Setting Header

ASCII: `~*`

`~*`: Header of settings command

### Setting Body

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

### Setting Tail

ASCII: `,000,00,1270,1270`

`000` increment: 0

`00` interval: 0

`1270` x-resolution: 1270

`1270` y-resolution: 1270