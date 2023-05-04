import serial
from internal_constants import *
from user_constants import *
import time

def setup_wacom_iv_1_0_to_1_1(port = SERIAL_PORT_PATH, baudrate = SERIAL_PORT_INITIAL_BAUD_RATE, bytesize = SERIAL_PORT_BYTESIZE, timeout = SERIAL_PORT_TIMEOUT, stopbits = SERIAL_PORT_STOPBITS):
    serial_port = serial.Serial(port = port, baudrate = baudrate, bytesize = bytesize, timeout = timeout, stopbits = stopbits)

    print("Setting up tablet, please wait. Do not put the pen on the tablet.")

    serial_port.write((WACOM_IV_1_0_TO_1_1_SETTINGS_COMMAND + "\r").encode())
    time.sleep(0.2)
    serial_port.baudrate = SERIAL_PORT_FINAL_BAUD_RATE
    time.sleep(0.2)

    print("Tablet setup finished.")

    return serial_port