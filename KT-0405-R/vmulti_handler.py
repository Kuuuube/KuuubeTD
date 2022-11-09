from pywinusb import hid
import constants

report_buffer = [0x00]*65

def find_device():
    all_devices = hid.HidDeviceFilter(vendor_id = constants.VMULTI_DEVICE_VENDOR_ID, product_id = constants.VMULTI_DEVICE_PRODUCT_ID,).get_devices()

    if len(all_devices) > 0:
        virtual_device = all_devices[-1]
        return virtual_device

    else:
        raise Exception("Virtual Multitouch Device driver not loaded.")

def send_report(report, pos_x, pos_y, pressure, press, proximity):    
    button_flags = 0

    button_flags = set_bit(button_flags, 0) if press else unset_bit(button_flags, 0)
    button_flags = set_bit(button_flags, 4) if proximity else unset_bit(button_flags, 4)

    report_buffer[0] = constants.VMULTI_ID
    report_buffer[1] = 12
    report_buffer[2] = constants.OUTPUT_MODE
    report_buffer[3] = button_flags

    scaled_pos_x = int(constants.VMULTI_MONITOR_SCALING_X * pos_x + constants.VMULTI_MONITOR_OFFSET_X)
    report_buffer[4] = scaled_pos_x & 0x00FF
    report_buffer[5] = (scaled_pos_x & 0xFF00) >> 8

    scaled_pos_y = int(constants.VMULTI_MONITOR_SCALING_Y * pos_y + constants.VMULTI_MONITOR_OFFSET_Y)
    report_buffer[6] = scaled_pos_y & 0x00FF
    report_buffer[7] = (scaled_pos_y & 0xFF00) >> 8

    scaled_pressure = pressure * 32
    report_buffer[8] = scaled_pressure & 0x00FF
    report_buffer[9] = (scaled_pressure & 0xFF00) >> 8

    report.set_raw_data(report_buffer)
    report.send()

def set_bit(val: int, pos: int):
    return val | (1 << pos)

def unset_bit(val: int, pos: int):
    return val & ~(1 << pos)