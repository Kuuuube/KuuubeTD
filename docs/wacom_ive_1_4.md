# Wacom IVe 1.4:

## Usage

- Follow [General Usage](./general_usage.md)

- Run `KuuubeTD/wacom_ive_1_4_driver.py`

## Notes

### Settings Command Applied by Driver:

```
~*F233C910,000,00,2540,2540
```

### Setting Header

ASCII: `~*`

`~*`: Header of settings command

### Setting Body

Hex: `F233C910` Binary: `11110010001100111100100100010000`

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

`1` tilt mode: on

`0` MM command set: MM1201

`0` MM961 orientation: landscape

`0` BitPad II cursor data: 1234

`0` remote mode: off

### Setting Tail

ASCII: `,000,00,2540,2540`

`000` increment: 0

`00` interval: 0

`2540` x-resolution: 2540

`2540` y-resolution: 2540