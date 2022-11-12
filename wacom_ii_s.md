# Wacom II-S:

## Usage

- Follow [General Usage](./general_usage.md)

- Run `KuuubeTD/wacom_ii_s.py`

- Optionally, you can set the first three dip switches in DS 2 (Dip Switch Bank 2) to on. This will increase the baud rate to 19200 and allow the tablet to send at a faster rate. If you make this change you will also need to change `SERIAL_PORT_INITIAL_BAUD_RATE` in `internal_constants.py` to 19200.

## Notes

### Settings Commands Applied by Driver:

```
RE
PH1
AS1
IN0
SR
```

### Setting Data

`RE` reset to default command set

`PH1` pressure mode: on

`AS1` data format: binary

`IN0` increment mode: 0

`SR` stream mode: on