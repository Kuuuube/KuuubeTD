import serial
from internal_constants import *
from user_constants import *
import time

def setup_wacom_ii_s(port = SERIAL_PORT_PATH, baudrate = SERIAL_PORT_INITIAL_BAUD_RATE, bytesize = SERIAL_PORT_BYTESIZE, timeout = SERIAL_PORT_TIMEOUT, stopbits = SERIAL_PORT_STOPBITS):
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