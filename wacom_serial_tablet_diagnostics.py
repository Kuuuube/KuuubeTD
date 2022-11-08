import serial
import time

SERIAL_PORT = 'COM3'
SERIAL_RATE = 19200
BYTE_SIZE = 8
STOPBITS = 1

def send_command(command, command_name):
    print("Attempting to send " + command_name + " command: ")
    serial_port.write((command + "\r").encode())
    output = serial_port.readline()
    print("UTF-8: ", end="")
    print(output.decode('utf-8'))
    time.sleep(0.2)

serial_port = serial.Serial(port=SERIAL_PORT, baudrate=SERIAL_RATE, bytesize=BYTE_SIZE, stopbits=STOPBITS, timeout=1)

baud_rates = [9600, 19200, 4800, 2400]

for baud_rate in baud_rates:
    serial_port.baudrate = baud_rate
    print("Testing " + str(baud_rate) + " baud rate")
    send_command("~#", "Tablet ID")
    send_command("~R", "Read Setting")
    send_command("~C", "Tablet Size")