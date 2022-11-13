import serial
import serial.tools.list_ports
import re
import serial_port_handler
import sys
import time
import os

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

print("Enter baud rate:")
SERIAL_RATE = input()

BYTE_SIZE = 8
STOPBITS = 1

print("Select parser:\n1. Wacom IVe 1.4\n2. Wacom IV 1.2-1.4\n3. Wacom IV 1.0-1.1\n4. Wacom II-S")
selected_parser = input()

print("Init tablet? (y/n):")
init = input()



if (init.lower() == "y"):
    if (selected_parser == "1"):
        serial_port = serial_port_handler.setup_wacom_ive_1_4()

    elif (selected_parser == "2"):
        serial_port = serial_port_handler.setup_wacom_iv_1_2_to_1_4()

    elif (selected_parser == "3"):
        serial_port = serial_port_handler.setup_wacom_iv_1_0_to_1_1()

    elif (selected_parser == "4"):
        serial_port = serial_port_handler.setup_wacom_ii_s()
    
    else:
        print("Invalid parser selected. Valid inputs are: (1/2/3/4)")
        sys.exit()
else:
    serial_port = serial.Serial(port = SERIAL_PORT, baudrate = SERIAL_RATE, bytesize = BYTE_SIZE, timeout = 1, stopbits = STOPBITS)

if (selected_parser == "1"):

    os.system('cls' if os.name == 'nt' else 'clear')
    print("Parser data:\n")

    while (True):
        try:
            report_parsed = serial_port_handler.read_data_wacom_ive_1_4(serial_port)

            sys.stdout.write("\033[F") # Reset line
            sys.stdout.write("\033[K") # Remove the previously printed line

            print("Proximity:" + str(report_parsed[0]) + " Pointer:" + str(report_parsed[1]) + " Button_Flag:" + str(report_parsed[2]) + " Position:[" + str(report_parsed[3]) + "," + str(report_parsed[4]) + "] Buttons:" + str(report_parsed[5]) + " Pressure:" + str(report_parsed[6]) + " Tilt:[" + str(report_parsed[7]) + ","  +  str(report_parsed[8]) + "]")
            
        except Exception as e:
            print(e)
            time.sleep(0.1)

elif (selected_parser == "2"):

    os.system('cls' if os.name == 'nt' else 'clear')
    print("Parser data:\n")

    while (True):
        try:
            report_parsed = serial_port_handler.read_data_wacom_iv_1_2_to_1_4(serial_port)

            sys.stdout.write("\033[F") # Reset line
            sys.stdout.write("\033[K") # Remove the previously printed line

            print("Proximity: " + str(report_parsed[0]) + ", Pointer: " + str(report_parsed[1]) + ", Button Flag: " + str(report_parsed[2]) + ", Pos X: " + str(report_parsed[3]) + ", Pos Y: " + str(report_parsed[4]) + ", Buttons: " + str(report_parsed[5]) + ", Pressure: " + str(report_parsed[6]))
            
        except Exception as e:
            print(e)
            time.sleep(0.1)

elif (selected_parser == "3"):

    os.system('cls' if os.name == 'nt' else 'clear')
    print("Parser data:\n")

    while (True):
        try:
            report_parsed = serial_port_handler.read_data_wacom_iv_1_0_to_1_1(serial_port)

            sys.stdout.write("\033[F") # Reset line
            sys.stdout.write("\033[K") # Remove the previously printed line

            print("Proximity: " + str(report_parsed[0]) + ", Pointer: " + str(report_parsed[1]) + ", Button Flag: " + str(report_parsed[2]) + ", Pos X: " + str(report_parsed[3]) + ", Pos Y: " + str(report_parsed[4]) + ", Buttons: " + str(report_parsed[5]) + ", Pressure: " + str(report_parsed[6]))
            
        except Exception as e:
            print(e)
            time.sleep(0.1)

elif (selected_parser == "4"):

    os.system('cls' if os.name == 'nt' else 'clear')
    print("Parser data:\n")

    while (True):
        try:
            report_parsed = serial_port_handler.read_data_wacom_ii_s(serial_port)

            sys.stdout.write("\033[F") # Reset line
            sys.stdout.write("\033[K") # Remove the previously printed line

            print("Proximity: " + str(report_parsed[0]) + ", Pointer: " + str(report_parsed[1]) + ", Pos X: " + str(report_parsed[2]) + ", Pos Y: " + str(report_parsed[3]) + ", Buttons: " + str(report_parsed[4]) + ", Button Flag: " + str(report_parsed[5]) + ", Pressure: " + str(report_parsed[6]))
        
        except Exception as e:
            print(e)
            time.sleep(0.1)

else:
    print("Invalid parser selected. Valid inputs are: (1/2/3/4)")
    sys.exit()