def parse(report):
    int.from_bytes(report[0:1], byteorder='big')

    pos_x: int = (
        ((int.from_bytes(report[0:1], byteorder='big') & 0x03) << 14)
        + (int.from_bytes(report[1:2], byteorder='big') << 7)
        + int.from_bytes(report[2:3], byteorder='big')
    )

    pos_y: int = (
        ((int.from_bytes(report[3:4], byteorder='big') & 0x03) << 14)
        + (int.from_bytes(report[4:5], byteorder='big') << 7)
        + int.from_bytes(report[5:6], byteorder='big')
    )

    pressure = (
        ((int.from_bytes(report[6:7], byteorder='big') & 0x7f) * 2)
        + ((int.from_bytes(report[3:4], byteorder='big') & 0x04) >> 2)
    )

    if (int.from_bytes(report[6:7], byteorder='big') & 0x40):
        pressure = (~(pressure - 1) & 0x7f) * -1

    pressure = pressure + 127

    button_pressed = bool(int.from_bytes(report[0:1], byteorder='big') & 0x08)

    proximity = bool(int.from_bytes(report[0:1], byteorder='big') & 0x40)

    button = int.from_bytes(report[3:4], byteorder='big') >> 3 if button_pressed else 0

    press = button == 1

    return (pos_x, pos_y, pressure, press, proximity)