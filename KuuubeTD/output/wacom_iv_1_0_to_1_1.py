from pywinusb import hid
from internal_constants import *
from user_constants import *
import tablet_monitor_mapping

report = [0x00]*65

def find_vmulti_device():
    all_devices = hid.HidDeviceFilter(vendor_id = VMULTI_DEVICE_VENDOR_ID, product_id = VMULTI_DEVICE_PRODUCT_ID,).get_devices()

    if len(all_devices) > 0:
        virtual_device = all_devices[-1]
        return virtual_device

    else:
        raise Exception("Virtual Multitouch Device driver not loaded.")

def send_vmulti_report_wacom_iv_1_0_to_1_1(vmulti_device_report, proximity, pointer, button_flag, pos_x, pos_y, buttons, pressure):    
    report[0] = VMULTI_ID
    report[1] = USAGE_PAGE_DIGITIZER
    report[2] = OUTPUT_MODE

    flags = 0
    if (button_flag):
        if (pointer):
            if (bool((buttons & 0x01))): # pen tip
                flags = flags | int(0x01) # pen tip

            if (bool((buttons & 0x02))): # bottom pen button
                flags = flags | int(0x02) # barrel button

            #if (bool((buttons & 0x04))): # top pen button
            #    flags = flags | int(0x02) # barrel button

            if (bool((buttons & 0x04))): # eraser
                flags = flags | int(0x08) # invert
        else:
            # tablet and mouse buttons are not implemented
            pass
    
    if (proximity):
        flags = flags | int(0x10)

    report[3] = flags

    scaled_pos_x = tablet_monitor_mapping.map_x(pos_x)
    report[4] = scaled_pos_x & 0x00FF
    report[5] = (scaled_pos_x & 0xFF00) >> 8

    scaled_pos_y = tablet_monitor_mapping.map_y(pos_y)
    report[6] = scaled_pos_y & 0x00FF
    report[7] = (scaled_pos_y & 0xFF00) >> 8

    scaled_pressure = 0
    if pressure > PRESSURE_DEADZONE:
        scaled_pressure = int(pressure + PRESSURE_OFFSET / WACOM_IV_1_0_TO_1_1_MAX_PRESSURE * 8191)
        if scaled_pressure < 0:
            scaled_pressure = 0
    report[8] = scaled_pressure & 0x00FF
    report[9] = (scaled_pressure & 0xFF00) >> 8

    vmulti_device_report.set_raw_data(report)
    vmulti_device_report.send()