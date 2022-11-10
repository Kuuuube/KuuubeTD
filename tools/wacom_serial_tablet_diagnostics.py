import serial
import time
import serial.tools.list_ports
import re

ports = serial.tools.list_ports.comports()

print("Available ports:")

for port in sorted(ports):
    try:
        print(re.sub(" .*", "", str(port)))
    except Exception:
        print(port)
print("")

print("Enter serial port path for tablet:")

SERIAL_PORT = input()
SERIAL_RATE = 9600
BYTE_SIZE = 8
STOPBITS = 1

def send_command(command, command_name):
    serial_port.write((command + "\r").encode())
    output = serial_port.readline()
    if (output != b""):
        print(command_name + ": ", end="")
        print(output.decode('utf-8'))
    time.sleep(0.2)

serial_port = serial.Serial(port=SERIAL_PORT, baudrate=SERIAL_RATE, bytesize=BYTE_SIZE, stopbits=STOPBITS, timeout=1)

baud_rates = [9600, 19200, 4800, 2400]

print("Attempting to request tablet information. Do not put your pen on the tablet.")

for baud_rate in baud_rates:
    serial_port.baudrate = baud_rate
    print("Testing " + str(baud_rate) + " baud rate")
    send_command("~#", "Tablet ID")
    send_command("~R", "Read Setting")
    send_command("~C", "Tablet Size")

print("Finished")
input()
