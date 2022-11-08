import serial


SERIAL_PORT = 'COM3'
SERIAL_RATE = 9600
BYTE_SIZE = 8
STOPBITS = 1
PARITY = 'N'

ser = serial.Serial(port=SERIAL_PORT, baudrate=SERIAL_RATE, bytesize=BYTE_SIZE, parity=PARITY, stopbits=STOPBITS, timeout=1)

report_number = 0

while True:
    report = ser.read(BYTE_SIZE - STOPBITS)

    if(len(report) > 0):
        print(str(report_number) + ": ", end =" ")
        
    for byte in report:
        print("{:08b}".format(byte), end =" ")

    if(len(report) > 0):
        print("")
        
        report_number += 1
