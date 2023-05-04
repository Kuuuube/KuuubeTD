import sys
import parsers.wacom_iv_1_2_to_1_4
import tablet_setup.wacom_iv_1_2_to_1_4
import output.wacom_iv_1_2_to_1_4
from internal_constants import *
from user_constants import *

vmulti_device = None
try:
    vmulti_device = output.wacom_iv_1_2_to_1_4.find_vmulti_device()
except Exception as e:
    print(e)
    sys.exit()
vmulti_device.open()

vmulti_device_report = vmulti_device.find_output_reports()[-1]

try:
    serial_port = tablet_setup.wacom_iv_1_2_to_1_4.setup_wacom_iv_1_2_to_1_4()
except Exception as e:
    print("Serial device setup failed.")
    print(e)
    sys.exit()

while(True):
    report = bytes(b"")
    while (len(report) != (SERIAL_PORT_WACOM_IV_1_2_TO_1_4_REPORT_SIZE)):
        report = serial_port.read(SERIAL_PORT_WACOM_IV_1_2_TO_1_4_REPORT_SIZE)

    report_parsed = parsers.wacom_iv_1_2_to_1_4.wacom_iv_1_2_to_1_4_parser(report)

    output.wacom_iv_1_2_to_1_4.send_vmulti_report_wacom_iv_1_2_to_1_4(vmulti_device_report, report_parsed[0], report_parsed[1], report_parsed[2], report_parsed[3], report_parsed[4], report_parsed[5], report_parsed[6])
