import sys
import parsers.wacom_ii
import tablet_setup.wacom_ii
import output.wacom_ii
import vmulti_device_handler
from internal_constants import *
from user_constants import *

vmulti_device = None
try:
    vmulti_device = vmulti_device_handler.find_vmulti_device()
except Exception as e:
    print(e)
    sys.exit()
vmulti_device.open()

vmulti_device_report = vmulti_device.find_output_reports()[-1]

try:
    serial_port = tablet_setup.wacom_ii.setup_wacom_ii()
except Exception as e:
    print("Serial device setup failed.")
    print(e)
    sys.exit()

while(True):
    report = bytes(b"")
    while (len(report) != (SERIAL_PORT_WACOM_II_REPORT_SIZE)):
        report = serial_port.read(SERIAL_PORT_WACOM_II_REPORT_SIZE)

    report_parsed = parsers.wacom_ii.wacom_ii_parser(report)

    output.wacom_ii.send_vmulti_report_wacom_ii(vmulti_device_report, report_parsed[0], report_parsed[1], report_parsed[2], report_parsed[3], report_parsed[4], report_parsed[5], report_parsed[6])
