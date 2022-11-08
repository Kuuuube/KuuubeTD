import serial
import constants
import time
import KT_0405_R_parser

def setup():
    serial_port = serial.Serial(port = constants.SERIAL_PORT_PATH,
    baudrate = constants.SERIAL_PORT_INITIAL_BAUD_RATE,
    bytesize = constants.SERIAL_PORT_BYTESIZE,
    timeout = constants.SERIAL_PORT_TIMEOUT,
    stopbits = constants.SERIAL_PORT_STOPBITS,
    )

    print("Setting up tablet, please wait. Do not put the pen on the tablet.")

    serial_port.write(constants.WACOM_COMMAND_RESET_WACOM_IV.encode())
    time.sleep(0.2)
    serial_port.write(constants.KT_0405_R_SETTINGS_COMMAND.encode())
    time.sleep(0.2)
    serial_port.baudrate = constants.SERIAL_PORT_FINAL_BAUD_RATE
    time.sleep(0.2)
    serial_port.write(constants.KT_0405_R_RESOLUTION_COMMAND.encode())

    print("Tablet setup finished.")

    return serial_port

def read_data(serial_port):
    report = bytes(b"")
    while (report == b""):
        report = serial_port.read(7)

    print(report)
    report_parsed = KT_0405_R_parser.parse(report)
    return report_parsed