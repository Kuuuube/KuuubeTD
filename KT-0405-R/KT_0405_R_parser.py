def parse(report):
    pos_x = (((int(report[0]) & 0x03) << 14) + (int(report[1]) << 7) + int(report[2]))

    pos_y = (((int(report[3]) & 0x03) << 14) + (int(report[4]) << 7) + int(report[5]))

    pressure = (((int(report[6]) & 0x7f) * 2) + ((int(report[3]) & 0x04) >> 2))

    if (int(report[6]) & 0x40):
        pressure = (~(pressure - 1) & 0x7f) * -1

    pressure = pressure + 127

    button_pressed = bool(int(report[0]) & 0x08)

    proximity = bool(int(report[0]) & 0x40)

    button = int(report[3]) >> 3 if button_pressed else 0

    pen_tip_press = bool(button & 0x01)

    return (pos_x, pos_y, pressure, pen_tip_press, proximity)