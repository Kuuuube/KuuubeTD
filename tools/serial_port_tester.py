import serial

SERIAL_PORT = 'COM3'

ser = serial.Serial(SERIAL_PORT)

while True:
    print(ser.read())
