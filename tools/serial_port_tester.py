import serial

SERIAL_PORT = 'COM3'

ser = serial.Serial(SERIAL_PORT, timeout=1)

while True:
    data = ser.read()
    if (data != b''):
        print(data)
