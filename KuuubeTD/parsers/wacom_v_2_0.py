def wacom_v_2_0_parser(report):
    pos_x = (((int(report[1]) & 0x7f) <<  9) + ((int(report[2]) & 0x7f) << 2) + ((int(report[3]) & 0x60) >> 5))

    pos_y = (((int(report[3]) & 0x1f) << 11) + ((int(report[4]) & 0x7f) << 4) + ((int(report[5]) & 0x78) >> 3))

    pressure = (((int(report[5]) & 0x07) << 7) + (int(report[6]) & 0x7f))

    proximity = bool(int(report[0]) & 0x40)

    pointer = bool(0)

    button_flag = bool(0)

    buttons = int(report[0]) & 0x06

    tilt_x = (int(report[7]) & 0x7F) - 64

    tilt_y = (int(report[8]) & 0x7F) - 64

    return (proximity, pointer, button_flag, pos_x, pos_y, buttons, pressure, tilt_x, tilt_y)
