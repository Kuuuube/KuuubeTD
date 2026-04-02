import time

import serial
from internal_constants import (
    SERIAL_PORT_BYTESIZE,
    SERIAL_PORT_INITIAL_BAUD_RATE,
    SERIAL_PORT_STOPBITS,
    SERIAL_PORT_TIMEOUT,
    WACOM_II_AND_II_S_BINARY_MODE_COMMAND,
    WACOM_II_AND_II_S_INCREMENT_COMMAND,
    WACOM_II_AND_II_S_OPERATION_MODE_COMMAND,
    WACOM_II_AND_II_S_PRESSURE_MODE_COMMAND,
    WACOM_II_AND_II_S_RESET_COMMAND,
)
from user_constants import SERIAL_PORT_PATH


def setup_wacom_ii(port: str = SERIAL_PORT_PATH, baudrate: int = SERIAL_PORT_INITIAL_BAUD_RATE, bytesize: int = SERIAL_PORT_BYTESIZE, timeout: int = SERIAL_PORT_TIMEOUT, stopbits: int = SERIAL_PORT_STOPBITS) -> serial.Serial:
    serial_port = serial.Serial(port = port, baudrate = baudrate, bytesize = bytesize, timeout = timeout, stopbits = stopbits)

    print("Setting up tablet, please wait. Do not put the pen on the tablet.")

    serial_port.write((WACOM_II_AND_II_S_RESET_COMMAND + "\r").encode())
    time.sleep(0.2)
    serial_port.write((WACOM_II_AND_II_S_PRESSURE_MODE_COMMAND + "\r").encode())
    time.sleep(0.2)
    serial_port.write((WACOM_II_AND_II_S_BINARY_MODE_COMMAND + "\r").encode())
    time.sleep(0.2)
    serial_port.write((WACOM_II_AND_II_S_INCREMENT_COMMAND + "\r").encode())
    time.sleep(0.2)
    serial_port.write((WACOM_II_AND_II_S_OPERATION_MODE_COMMAND + "\r").encode())
    time.sleep(0.2)

    print("Tablet setup finished.")

    return serial_port
