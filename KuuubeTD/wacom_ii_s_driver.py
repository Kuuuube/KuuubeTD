import vmulti_handler
import sys
import serial_port_handler

vmulti_device = None
try:
    vmulti_device = vmulti_handler.find_device()
except Exception as e:
    print(e)
    sys.exit()
vmulti_device.open()

vmulti_device_report = vmulti_device.find_output_reports()[-1]

try:
    serial_port = serial_port_handler.setup_wacom_ii_s()
except Exception as e:
    print("Serial device setup failed.")
    print(e)
    sys.exit()

while(True):
    report_parsed = serial_port_handler.read_data_wacom_ii_s(serial_port)
    vmulti_handler.send_report_wacom_ii_s(vmulti_device_report, report_parsed[0], report_parsed[1], report_parsed[2], report_parsed[3], report_parsed[4], report_parsed[5], report_parsed[6])
