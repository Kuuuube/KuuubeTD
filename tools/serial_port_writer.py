import serial
import time

SERIAL_PORT = "COM3"
SERIAL_RATE = 9600
BYTE_SIZE = 8
STOPBITS = 1

def send_command(command, command_name):
    serial_port.write((command + "\r").encode())
    while True:
        output = serial_port.readline()
        if (output != b""):
            print(command_name + ": ", end="")
            print(output.decode('utf-8'))
        else:
            break
    time.sleep(0.2)

serial_port = serial.Serial(port=SERIAL_PORT, baudrate=SERIAL_RATE, bytesize=BYTE_SIZE, stopbits=STOPBITS, timeout=1)

while (True):
    print("Enter command: ")
    command = input()
    send_command(command, "Output")
