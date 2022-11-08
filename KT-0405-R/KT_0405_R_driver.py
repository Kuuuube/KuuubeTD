import vmulti_handler
import sys
import serial_port_handler

#vmulti

vmulti_device = None
try:
    vmulti_device = vmulti_handler.find_device()
except Exception as e:
    print(e)
    sys.exit()
vmulti_device.open()

report = vmulti_device.find_output_reports()[-1]

#serial

serial_port = serial_port_handler.setup()

import datetime
while(True):
    start_time = datetime.datetime.now()
    report_parsed = serial_port_handler.read_data(serial_port)
    vmulti_handler.send_report(report, report_parsed[0], report_parsed[1], report_parsed[2], report_parsed[3], report_parsed[4])
    end_time = datetime.datetime.now()
    print(end_time - start_time)