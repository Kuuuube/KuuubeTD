import serial
from internal_constants import *
from user_constants import *
import time
import parser

def setup_wacom_ive_1_4():
    serial_port = serial.Serial(port = SERIAL_PORT_PATH,
    baudrate = SERIAL_PORT_INITIAL_BAUD_RATE,
    bytesize = SERIAL_PORT_BYTESIZE,
    timeout = SERIAL_PORT_TIMEOUT,
    stopbits = SERIAL_PORT_STOPBITS,
    )

    print("Setting up tablet, please wait. Do not put the pen on the tablet.")

    serial_port.write((WACOM_IVE_1_4_SETTINGS_COMMAND + "\r").encode())
    time.sleep(0.2)
    serial_port.baudrate = SERIAL_PORT_FINAL_BAUD_RATE
    time.sleep(0.2)

    print("Tablet setup finished.")

    return serial_port

def setup_wacom_iv_1_2_to_1_4():
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

def setup_wacom_iv_1_0_to_1_1():
    serial_port = serial.Serial(port = SERIAL_PORT_PATH,
    baudrate = SERIAL_PORT_INITIAL_BAUD_RATE,
    bytesize = SERIAL_PORT_BYTESIZE,
    timeout = SERIAL_PORT_TIMEOUT,
    stopbits = SERIAL_PORT_STOPBITS,
    )

    print("Setting up tablet, please wait. Do not put the pen on the tablet.")

    serial_port.write((WACOM_IV_1_0_TO_1_1_SETTINGS_COMMAND + "\r").encode())
    time.sleep(0.2)
    serial_port.baudrate = SERIAL_PORT_FINAL_BAUD_RATE
    time.sleep(0.2)

    print("Tablet setup finished.")

    return serial_port

def setup_wacom_ii_s():
    serial_port = serial.Serial(port = SERIAL_PORT_PATH,
    baudrate = SERIAL_PORT_INITIAL_BAUD_RATE,
    bytesize = SERIAL_PORT_BYTESIZE,
    timeout = SERIAL_PORT_TIMEOUT,
    stopbits = SERIAL_PORT_STOPBITS,
    )

    print("Setting up tablet, please wait. Do not put the pen on the tablet.")

    serial_port.write((WACOM_II_S_RESET_COMMAND + "\r").encode())
    time.sleep(0.2)
    serial_port.write((WACOM_II_S_PRESSURE_MODE_COMMAND + "\r").encode())
    time.sleep(0.2)
    serial_port.write((WACOM_II_S_BINARY_MODE_COMMAND + "\r").encode())
    time.sleep(0.2)
    serial_port.write((WACOM_II_S_INCREMENT_COMMAND + "\r").encode())
    time.sleep(0.2)
    serial_port.write((WACOM_II_S_OPERATION_MODE_COMMAND + "\r").encode())
    time.sleep(0.2)

    print("Tablet setup finished.")

    return serial_port

def read_data_wacom_ive_1_4(serial_port):
    report = bytes(b"")
    while (len(report) != (SERIAL_PORT_WACOM_IVE_1_4_REPORT_SIZE)):
        report = serial_port.read(SERIAL_PORT_WACOM_IVE_1_4_REPORT_SIZE)

    report_parsed = parser.wacom_ive_1_4_parser(report)
    return report_parsed

def read_data_wacom_iv_1_2_to_1_4(serial_port):
    report = bytes(b"")
    while (len(report) != (SERIAL_PORT_WACOM_IV_1_2_TO_1_4_REPORT_SIZE)):
        report = serial_port.read(SERIAL_PORT_WACOM_IV_1_2_TO_1_4_REPORT_SIZE)

    report_parsed = parser.wacom_iv_1_2_to_1_4_parser(report)
    return report_parsed

def read_data_wacom_iv_1_0_to_1_1(serial_port):
    report = bytes(b"")
    while (len(report) != (SERIAL_PORT_WACOM_IV_1_0_TO_1_1_REPORT_SIZE)):
        report = serial_port.read(SERIAL_PORT_WACOM_IV_1_0_TO_1_1_REPORT_SIZE)

    report_parsed = parser.wacom_iv_1_0_to_1_1_parser(report)
    return report_parsed

def read_data_wacom_ii_s(serial_port):
    report = bytes(b"")
    while (len(report) != (SERIAL_PORT_WACOM_II_S_REPORT_SIZE)):
        report = serial_port.read(SERIAL_PORT_WACOM_II_S_REPORT_SIZE)

    report_parsed = parser.wacom_ii_s_parser(report)
    return report_parsed