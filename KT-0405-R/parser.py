def parse(report):
    pos_x = (((int(report[0]) & 0x03) << 14) + (int(report[1]) << 7) + int(report[2]))

    pos_y = (((int(report[3]) & 0x03) << 14) + (int(report[4]) << 7) + int(report[5]))

    pressure = (((int(report[6]) & 0x3f) << 1) + ((int(report[3]) & 0x04) >> 2))

    if (int(report[6]) & 0x40 == 0):
        pressure = pressure + int(0x80)

    proximity = bool(int(report[0]) & 0x40)

    button_flag = bool(int(report[0]) & 0x08)

    pen_tip = bool(int(report[3]) & 0x08)

    top_side_button_or_eraser = bool(int(report[3]) & 0x20)

    bottom_side_button = bool(int(report[3]) & 0x10)

    return (pos_x, pos_y, pressure, pen_tip, proximity)