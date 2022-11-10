from pywinusb import hid
import constants

report = [0x00]*65

def find_device():
    all_devices = hid.HidDeviceFilter(vendor_id = constants.VMULTI_DEVICE_VENDOR_ID, product_id = constants.VMULTI_DEVICE_PRODUCT_ID,).get_devices()

    if len(all_devices) > 0:
        virtual_device = all_devices[-1]
        return virtual_device

    else:
        raise Exception("Virtual Multitouch Device driver not loaded.")

def send_report(vmulti_device_report, pos_x, pos_y, pressure, press, proximity, pen_button, eraser):    
    report[0] = constants.VMULTI_ID
    report[1] = constants.USAGE_PAGE_DIGITIZER
    report[2] = constants.OUTPUT_MODE

    button_flags = 0

    if (press):
        button_flags += int(0x01)

    if (pen_button):
        button_flags += int(0x02)

    if (eraser):
        button_flags += int(0x08)

    if (proximity):
        button_flags += int(0x10)


    report[3] = button_flags

    scaled_pos_x = int(constants.VMULTI_MONITOR_SCALING_X * (pos_x - constants.TABLET_OFFSET_X) + constants.VMULTI_MONITOR_OFFSET_X)
    report[4] = scaled_pos_x & 0x00FF
    report[5] = (scaled_pos_x & 0xFF00) >> 8

    scaled_pos_y = int(constants.VMULTI_MONITOR_SCALING_Y * (pos_y - constants.TABLET_OFFSET_Y) + constants.VMULTI_MONITOR_OFFSET_Y)
    report[6] = scaled_pos_y & 0x00FF
    report[7] = (scaled_pos_y & 0xFF00) >> 8

    scaled_pressure = pressure * 32
    report[8] = scaled_pressure & 0x00FF
    report[9] = (scaled_pressure & 0xFF00) >> 8

    vmulti_device_report.set_raw_data(report)
    vmulti_device_report.send()