import serial
import serial.tools.list_ports
import re
import parsers.wacom_v_2_0, parsers.wacom_ive_1_4, parsers.wacom_iv_1_2_to_1_4, parsers.wacom_iv_1_0_to_1_1, parsers.wacom_ii_s, parsers.wacom_ii
import tablet_setup.wacom_v_2_0, tablet_setup.wacom_ive_1_4, tablet_setup.wacom_iv_1_2_to_1_4, tablet_setup.wacom_iv_1_0_to_1_1, tablet_setup.wacom_ii_s, tablet_setup.wacom_ii
import sys
import time
import os
from internal_constants import *

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

print("Select parser:1. Wacom V 2.0\n2. Wacom IVe 1.4\n3. Wacom IV 1.2-1.4\n4. Wacom IV 1.0-1.1\n5. Wacom II-S\n6. Wacom II")
selected_parser = input()

print("Init tablet? (y/n):")
init = input()



if (init.lower() == "y"):
    if (selected_parser == "1"):
        serial_port = tablet_setup.wacom_v_2_0.setup_wacom_v_2_0(port = SERIAL_PORT, baudrate = SERIAL_RATE, bytesize = BYTE_SIZE, timeout = 1, stopbits = STOPBITS)

    elif (selected_parser == "2"):
        serial_port = tablet_setup.wacom_ive_1_4.setup_wacom_ive_1_4(port = SERIAL_PORT, baudrate = SERIAL_RATE, bytesize = BYTE_SIZE, timeout = 1, stopbits = STOPBITS)

    elif (selected_parser == "3"):
        serial_port = tablet_setup.wacom_iv_1_2_to_1_4.setup_wacom_iv_1_2_to_1_4(port = SERIAL_PORT, baudrate = SERIAL_RATE, bytesize = BYTE_SIZE, timeout = 1, stopbits = STOPBITS)

    elif (selected_parser == "4"):
        serial_port = tablet_setup.wacom_iv_1_0_to_1_1.setup_wacom_iv_1_0_to_1_1(port = SERIAL_PORT, baudrate = SERIAL_RATE, bytesize = BYTE_SIZE, timeout = 1, stopbits = STOPBITS)

    elif (selected_parser == "5"):
        serial_port = tablet_setup.wacom_ii_s.setup_wacom_ii_s(port = SERIAL_PORT, baudrate = SERIAL_RATE, bytesize = BYTE_SIZE, timeout = 1, stopbits = STOPBITS)

    elif (selected_parser == "6"):
        serial_port = tablet_setup.wacom_ii.setup_wacom_ii(port = SERIAL_PORT, baudrate = SERIAL_RATE, bytesize = BYTE_SIZE, timeout = 1, stopbits = STOPBITS)
    
    else:
        print("Invalid parser selected. Valid inputs are: (1/2/3/4/5)")
        sys.exit()
else:
    serial_port = serial.Serial(port = SERIAL_PORT, baudrate = SERIAL_RATE, bytesize = BYTE_SIZE, timeout = 1, stopbits = STOPBITS)

if (selected_parser == "1"):

    os.system('cls' if os.name == 'nt' else 'clear')
    print("Parser data:\n")

    while (True):
        try:
            report = bytes(b"")
            while (len(report) != (SERIAL_PORT_WACOM_V_2_0_REPORT_SIZE)):
                report = serial_port.read(SERIAL_PORT_WACOM_V_2_0_REPORT_SIZE)

            report_parsed = parsers.wacom_v_2_0.wacom_v_2_0_parser(report)

            sys.stdout.write("\033[F") # Reset line
            sys.stdout.write("\033[K") # Remove the previously printed line

            print("Proximity:" + str(report_parsed[0]) + " Pointer:" + str(report_parsed[1]) + " Button_Flag:" + str(report_parsed[2]) + " Position:[" + str(report_parsed[3]) + "," + str(report_parsed[4]) + "] Buttons:" + str(report_parsed[5]) + " Pressure:" + str(report_parsed[6]) + " Tilt:[" + str(report_parsed[7]) + ","  +  str(report_parsed[8]) + "]")
            
        except Exception as e:
            print(e)
            time.sleep(0.1)

if (selected_parser == "2"):

    os.system('cls' if os.name == 'nt' else 'clear')
    print("Parser data:\n")

    while (True):
        try:
            report = bytes(b"")
            while (len(report) != (SERIAL_PORT_WACOM_IVE_1_4_REPORT_SIZE)):
                report = serial_port.read(SERIAL_PORT_WACOM_IVE_1_4_REPORT_SIZE)

            report_parsed = parsers.wacom_ive_1_4.wacom_ive_1_4_parser(report)

            sys.stdout.write("\033[F") # Reset line
            sys.stdout.write("\033[K") # Remove the previously printed line

            print("Proximity:" + str(report_parsed[0]) + " Pointer:" + str(report_parsed[1]) + " Button_Flag:" + str(report_parsed[2]) + " Position:[" + str(report_parsed[3]) + "," + str(report_parsed[4]) + "] Buttons:" + str(report_parsed[5]) + " Pressure:" + str(report_parsed[6]) + " Tilt:[" + str(report_parsed[7]) + ","  +  str(report_parsed[8]) + "]")
            
        except Exception as e:
            print(e)
            time.sleep(0.1)

elif (selected_parser == "3"):

    os.system('cls' if os.name == 'nt' else 'clear')
    print("Parser data:\n")

    while (True):
        try:
            report = bytes(b"")
            while (len(report) != (SERIAL_PORT_WACOM_IV_1_2_TO_1_4_REPORT_SIZE)):
                report = serial_port.read(SERIAL_PORT_WACOM_IV_1_2_TO_1_4_REPORT_SIZE)

            report_parsed = parsers.wacom_iv_1_2_to_1_4.wacom_iv_1_2_to_1_4_parser(report)

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
            report = bytes(b"")
            while (len(report) != (SERIAL_PORT_WACOM_IV_1_0_TO_1_1_REPORT_SIZE)):
                report = serial_port.read(SERIAL_PORT_WACOM_IV_1_0_TO_1_1_REPORT_SIZE)

            report_parsed = parsers.wacom_iv_1_0_to_1_1.wacom_iv_1_0_to_1_1_parser(report)

            sys.stdout.write("\033[F") # Reset line
            sys.stdout.write("\033[K") # Remove the previously printed line

            print("Proximity: " + str(report_parsed[0]) + ", Pointer: " + str(report_parsed[1]) + ", Button Flag: " + str(report_parsed[2]) + ", Pos X: " + str(report_parsed[3]) + ", Pos Y: " + str(report_parsed[4]) + ", Buttons: " + str(report_parsed[5]) + ", Pressure: " + str(report_parsed[6]))
            
        except Exception as e:
            print(e)
            time.sleep(0.1)

elif (selected_parser == "5"):

    os.system('cls' if os.name == 'nt' else 'clear')
    print("Parser data:\n")

    while (True):
        try:
            report = bytes(b"")
            while (len(report) != (SERIAL_PORT_WACOM_II_S_REPORT_SIZE)):
                report = serial_port.read(SERIAL_PORT_WACOM_II_S_REPORT_SIZE)

            report_parsed = parsers.wacom_ii_s.wacom_ii_s_parser(report)

            sys.stdout.write("\033[F") # Reset line
            sys.stdout.write("\033[K") # Remove the previously printed line

            print("Proximity: " + str(report_parsed[0]) + ", Pointer: " + str(report_parsed[1]) + ", Pos X: " + str(report_parsed[2]) + ", Pos Y: " + str(report_parsed[3]) + ", Buttons: " + str(report_parsed[4]) + ", Button Flag: " + str(report_parsed[5]) + ", Pressure: " + str(report_parsed[6]))
        
        except Exception as e:
            print(e)
            time.sleep(0.1)

elif (selected_parser == "6"):

    os.system('cls' if os.name == 'nt' else 'clear')
    print("Parser data:\n")

    while (True):
        try:
            report = bytes(b"")
            while (len(report) != (SERIAL_PORT_WACOM_II_REPORT_SIZE)):
                report = serial_port.read(SERIAL_PORT_WACOM_II_REPORT_SIZE)

            report_parsed = parsers.wacom_ii.wacom_ii_parser(report)

            sys.stdout.write("\033[F") # Reset line
            sys.stdout.write("\033[K") # Remove the previously printed line

            print("Proximity: " + str(report_parsed[0]) + ", Pointer: " + str(report_parsed[1]) + ", Pos X: " + str(report_parsed[2]) + ", Pos Y: " + str(report_parsed[3]) + ", Buttons: " + str(report_parsed[4]) + ", Button Flag: " + str(report_parsed[5]) + ", Pressure: " + str(report_parsed[6]))
        
        except Exception as e:
            print(e)
            time.sleep(0.1)

else:
    print("Invalid parser selected. Valid inputs are: (1/2/3/4)")
    sys.exit()
