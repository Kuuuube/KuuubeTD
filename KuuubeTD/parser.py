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

    tilt_x = int(report[7]) & 0x3F

    if (int(report[7]) & 0x40 == 0):
        tilt_x = tilt_x * -1

    tilt_y = int(report[8]) & 0x3F

    if (int(report[8]) & 0x40 == 0):
        tilt_y = tilt_y * -1

    return (proximity, pointer, button_flag, pos_x, pos_y, buttons, pressure, tilt_x, tilt_y)

def wacom_iv_1_2_to_1_4_parser(report):
    pos_x = (((int(report[0]) & 0x03) << 14) + (int(report[1]) << 7) + int(report[2]))

    pos_y = (((int(report[3]) & 0x03) << 14) + (int(report[4]) << 7) + int(report[5]))

    pressure = (((int(report[6]) & 0x3f) << 1) + ((int(report[3]) & 0x04) >> 2))

    if (int(report[6]) & 0x40 == 0):
        pressure = pressure + int(0x80)

    proximity = bool(int(report[0]) & 0x40)

    pointer = bool(int(report[0]) & 0x20)

    button_flag = bool(int(report[0]) & 0x08)

    buttons = (int(report[3]) & 0x78) >> 3

    return (proximity, pointer, button_flag, pos_x, pos_y, buttons, pressure)

def wacom_iv_1_0_to_1_1_parser(report):
    pos_x = (((int(report[0]) & 0x03) << 14) + (int(report[1]) << 7) + int(report[2]))

    pos_y = (((int(report[3]) & 0x03) << 14) + (int(report[4]) << 7) + int(report[5]))

    pressure = int(report[6]) & 0x3f

    if (int(report[6]) & 0x40 == 0):
        pressure = pressure + int(0x40)

    proximity = bool(int(report[0]) & 0x40)

    pointer = bool(int(report[0]) & 0x20)

    button_flag = bool(int(report[0]) & 0x08)

    buttons = (int(report[3]) & 0x78) >> 3

    return (proximity, pointer, button_flag, pos_x, pos_y, buttons, pressure)

def wacom_ii_s_parser(report):
    pos_x = (((int(report[0]) & 0x03) << 14) + (int(report[1]) << 7) + int(report[2]))

    if ((int(report[0]) & 0x04) >> 2 == 1):
            pos_x = pos_x + int(0x10000)

    pos_y = (((int(report[3]) & 0x03) << 14) + (int(report[4]) << 7) + int(report[5]))

    if ((int(report[3]) & 0x04) >> 2 == 1):
            pos_y = pos_y + int(0x10000)

    proximity = bool(int(report[0]) & 0x40)

    pointer = bool(int(report[0]) & 0x20)

    pressure_mode = bool(int(report[0]) & 0x10)

    if (pressure_mode):
        pressure = int(report[6]) & 0x1F
        
        if (int(report[6]) & 0x40 == 0):
            if (((int((report[6]) & 0x20) >> 5)) == 1):
                pressure = pressure + int(0x20)

            pressure = pressure + int(0x20)

        button_flag = 0
        buttons = 0
    else:
        button_flag = bool((int(report[6]) & 0x20) >> 5)
        buttons = int(report[6]) & 0x1F

        pressure = 0

    return (proximity, pointer, pos_x, pos_y, buttons, button_flag, pressure)
