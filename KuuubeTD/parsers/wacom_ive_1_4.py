def wacom_ive_1_4_parser(report):
    pos_x = (((int(report[0]) & 0x03) << 14) + (int(report[1]) << 7) + int(report[2]))

    pos_y = (((int(report[3]) & 0x03) << 14) + (int(report[4]) << 7) + int(report[5]))

    pressure = (((int(report[6]) & 0x3f) << 1) + ((int(report[3]) & 0x04) >> 2))

    if (int(report[6]) & 0x40 == 0):
        pressure = pressure + int(0x80)

    proximity = bool(int(report[0]) & 0x40)

    pointer = bool(int(report[0]) & 0x20)

    button_flag = bool(int(report[0]) & 0x08)

    buttons = (int(report[3]) & 0x78) >> 3

    tilt_x = (int(report[7]) & 0x7F) - 64

    tilt_y = (int(report[8]) & 0x7F) - 64

    return (proximity, pointer, button_flag, pos_x, pos_y, buttons, pressure, tilt_x, tilt_y)