import time

import serial
from internal_constants import (
    SERIAL_PORT_BYTESIZE,
    SERIAL_PORT_FINAL_BAUD_RATE,
    SERIAL_PORT_INITIAL_BAUD_RATE,
    SERIAL_PORT_STOPBITS,
    SERIAL_PORT_TIMEOUT,
    WACOM_IVE_1_4_SETTINGS_COMMAND,
)
from user_constants import SERIAL_PORT_PATH


def setup_wacom_ive_1_4(port: str = SERIAL_PORT_PATH, baudrate: int = SERIAL_PORT_INITIAL_BAUD_RATE, bytesize: int = SERIAL_PORT_BYTESIZE, timeout: int = SERIAL_PORT_TIMEOUT, stopbits: int = SERIAL_PORT_STOPBITS) -> serial.Serial:
    serial_port = serial.Serial(port = port, baudrate = baudrate, bytesize = bytesize, timeout = timeout, stopbits = stopbits)

    print("Setting up tablet, please wait. Do not put the pen on the tablet.")

    serial_port.write((WACOM_IVE_1_4_SETTINGS_COMMAND + "\r").encode())
    time.sleep(0.2)
    serial_port.baudrate = SERIAL_PORT_FINAL_BAUD_RATE
    time.sleep(0.2)

    print("Tablet setup finished.")

    return serial_port
