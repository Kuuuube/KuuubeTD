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

def send_command(command, command_name, lines_to_read):
    serial_port.write((command + "\r").encode())
    lines_read = 0
    while (lines_read < lines_to_read):
        output = serial_port.readline()
        if (output != b""):
            print(command_name + ": ", end="")
            print(output.decode('utf-8'))
        lines_read += 1
    time.sleep(0.2)

serial_port = serial.Serial(port=SERIAL_PORT, baudrate=SERIAL_RATE, bytesize=BYTE_SIZE, stopbits=STOPBITS, timeout=1)

baud_rates = [9600, 19200, 4800, 2400]

print("Attempting to request tablet information. Do not put your pen on the tablet.")

for baud_rate in baud_rates:
    serial_port.baudrate = baud_rate
    print("Testing " + str(baud_rate) + " baud rate")
    send_command("~#", "Tablet ID", 1)
    send_command("~R", "Read Setting", 1)
    send_command("TE", "Test", 2)
    send_command("~C", "Tablet Size", 1)

print("Finished")
input()
