from pywinusb import hid
from internal_constants import *

def find_vmulti_device():
    all_devices = hid.HidDeviceFilter(vendor_id = VMULTI_DEVICE_VENDOR_ID, product_id = VMULTI_DEVICE_PRODUCT_ID,).get_devices()

    if len(all_devices) > 0:
        for device in all_devices:
            try:
                device.open()
                if device.find_output_reports():
                    return device
            finally:
                device.close()

    else:
        raise Exception("Virtual Multitouch Device driver not loaded.")