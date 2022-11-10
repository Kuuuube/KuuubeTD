import serial
from internal_constants import *
from user_constants import *
import time
import parser

def setup():
    serial_port = serial.Serial(port = SERIAL_PORT_PATH,
    baudrate = SERIAL_PORT_INITIAL_BAUD_RATE,
    bytesize = SERIAL_PORT_BYTESIZE,
    timeout = SERIAL_PORT_TIMEOUT,
    stopbits = SERIAL_PORT_STOPBITS,
    )

    print("Setting up tablet, please wait. Do not put the pen on the tablet.")

    serial_port.write((WACOM_IV_1_2_TO_1_4_SETTINGS_COMMAND + "\r").encode())
    time.sleep(0.2)
    serial_port.baudrate = SERIAL_PORT_FINAL_BAUD_RATE
    time.sleep(0.2)

    print("Tablet setup finished.")

    return serial_port

def read_data(serial_port):
    report = bytes(b"")
    while (len(report) != (SERIAL_PORT_BYTESIZE - SERIAL_PORT_STOPBITS)):
        report = serial_port.read(SERIAL_PORT_BYTESIZE - SERIAL_PORT_STOPBITS)

    report_parsed = parser.parse(report)
    return report_parsed