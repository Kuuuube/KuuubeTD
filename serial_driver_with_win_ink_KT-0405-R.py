import serial
import sys
import time

from pywinusb import hid

VIRTUAL_MULTITOUCH_DEVICE_VENDOR_ID = 0x00ff
VIRTUAL_MULTITOUCH_DEVICE_PRODUCT_ID = 0xbacc
VIRTUAL_MULTITOUCH_ID = 0x40
VIRTUAL_MULTITOUCH_REPORT_ID_WINDOWSINK = 0x05
VIRTUAL_MULTITOUCH_REPORT_ID_ABSOLUTE_POINTER = 0x09

WACOM_COMMAND_GET_TABLET_MODEL = '~#'
WACOM_COMMAND_SELF_TEST = 'TE'
WACOM_COMMAND_GET_CONFIG = '~R'
WACOM_COMMAND_GET_MAX_COORD = '~C'
WACOM_COMMAND_RESET_WACOM_IV = '#'

TABLET_MAX_X_POS = 6400
TABLET_MAX_Y_POS = 4800

ALL_MONITORS_RES_X = 3840
ALL_MONITORS_RES_Y = 1080
MAPPED_MONITOR_RES_X = 1920
MAPPED_MONITOR_RES_Y = 1080
OFFSET_X = 0
OFFSET_Y = 0

DEBUG_PRINTING = False

def set_bit(val: int, pos: int):
    return val | (1 << pos)

def unset_bit(val: int, pos: int):
    return val & ~(1 << pos)

class Tablet:
    res_x: int      = 0  # horizontal resolution of tablet
    res_y: int      = 0  # vertical resolution of tablet
    proximity: bool = 0  # is pen hovering over tablet
    press: bool     = 0  # is pen being pressed
    pos_x_old: int  = 0  # previous x position (for relative)
    pos_y_old: int  = 0  # previous y position (for relative)
    pos_x: int      = 0  # current x position
    pos_y: int      = 0  # current y position
    pressure: int   = 0  # current pressure
    #tilt_x: int     = 0  # tilt in the x axis
    #tilt_y: int     = 0  # tilt in the y axis

    def set_position(self, pos_x:int, pos_y:int):
        self.pos_x_old = self.pos_x
        self.pos_x = pos_x

        self.pos_y_old = self.pos_y
        self.pos_y = pos_y

    def set_pressure(self, pressure):
        self.pressure = pressure

    #def set_tilt(self, tilt_x:int, tilt_y:int):
    #    self.tilt_x = tilt_x
    #    self.tilt_y = tilt_y

class WacomSerialTablet(Tablet):
    serial_port: serial.Serial = None
    serial_buffer: bytearray = bytearray(1000)  # this gives us approximately a 1 second buffer at 9600 baud
    serial_buffer_write_index: int = 0          # index of buffer to be written
    serial_buffer_read_index: int = 0           # index of buffer to be read for parsing
    serial_buffer_packet: bytearray = bytearray(9)          # bytearray to hold a single packet
    serial_buffer_packet_index: int = 0

    tablet_model: str = None
    rom_version: str = None
    protocol: str = None

    def __init__(self, serial_port):
        print("Setting up tablet, please wait. Do not put the pen on the tablet.")
        self.serial_port = serial_port

        # query tablet for model and ROM version
        serial_port.write(f'{WACOM_COMMAND_GET_TABLET_MODEL}\r'.encode())

        # format: "~#{tablet_model} {rom_version}\r"
        # example: "~#UD-1212-R00 V1.5-4\r"
        try:
            model_and_rom_version = (
                serial_port.readline()
                .decode('utf-8')
                .replace(WACOM_COMMAND_GET_TABLET_MODEL, '')
                .replace('\r', '')
                .split(' ')
            )
            self.tablet_model = model_and_rom_version[0]
            self.rom_version = model_and_rom_version[1]
            if (DEBUG_PRINTING):
                print(f'Wacom Tablet Model: {self.tablet_model}')
                print(f'Wacom ROM Version: {self.rom_version}')
        except Exception:
            print("Failed to get tablet model. Restart the program and do not put your pen on the tablet until setup is finished.")

        if (DEBUG_PRINTING):
            print('Resetting tablet to Wacom IV command set...')
        serial_port.write(f'{WACOM_COMMAND_RESET_WACOM_IV}\r'.encode())
        # after resetting, tablet does not accept input for at least 10ms,
        # so we wait for 200ms
        time.sleep(0.2)

        # configure tablet + enable tilt (FM1)
        #serial_port.write(b'MU1\rOC1\r~M0\r~M1\r~IT0\rFM1\r')

        # format: "~R{setting_body},{increment},{interval},{res_x},{res_y}\r"
        # example: "~RE202C900,002,02,1270,1270\r"
        try:
            serial_port.write(f'{WACOM_COMMAND_GET_CONFIG}\r'.encode())
            config = (
                serial_port.readline()
                .decode('utf-8')
                .replace(WACOM_COMMAND_GET_CONFIG, '')
                .replace('\r', '')
                .split(',')
            )
            if (DEBUG_PRINTING):
                print(config[0])
                print(config[1])
                print(config[2])
                self.res_x = config[3]
                self.res_y = config[4]
                print(f'X Resolution: {self.res_x}, Y Resoluiton: {self.res_y}')
            print("Tablet ready for use.")
        except Exception:
            print("Failed to get resolution. Restart the program and do not put your pen on the tablet until setup is finished.")

    def parse_wacom_iv_packet(self):
        int.from_bytes(self.serial_buffer_packet[0:1], byteorder='big')

        pos_x: int = (
            ((int.from_bytes(self.serial_buffer_packet[0:1], byteorder='big') & 0x03) << 14)
            + (int.from_bytes(self.serial_buffer_packet[1:2], byteorder='big') << 7)
            + int.from_bytes(self.serial_buffer_packet[2:3], byteorder='big')
        )

        pos_y: int = (
            ((int.from_bytes(self.serial_buffer_packet[3:4], byteorder='big') & 0x03) << 14)
            + (int.from_bytes(self.serial_buffer_packet[4:5], byteorder='big') << 7)
            + int.from_bytes(self.serial_buffer_packet[5:6], byteorder='big')
        )

        pressure = (
            ((int.from_bytes(self.serial_buffer_packet[6:7], byteorder='big') & 0x7f) * 2)
            + ((int.from_bytes(self.serial_buffer_packet[3:4], byteorder='big') & 0x04) >> 2)
        )

        if (int.from_bytes(self.serial_buffer_packet[6:7], byteorder='big') & 0x40):
            pressure = (~(pressure - 1) & 0x7f) * -1

        pressure = pressure + 127

        #tilt_x = int.from_bytes(self.serial_buffer_packet[7:8], byteorder='big') & 0x7f
        #tilt_y = int.from_bytes(self.serial_buffer_packet[8:9], byteorder='big') & 0x7f

        #if (int.from_bytes(self.serial_buffer_packet[7:8], byteorder='big') & 0x40):
        #    tilt_x = (~(tilt_x - 1) & 0x7f) * -1

        #if (int.from_bytes(self.serial_buffer_packet[8:9], byteorder='big') & 0x40):
        #    tilt_y = (~(tilt_y - 1) & 0x7f) * -1

        # whether or not a button has been pressed
        button_pressed = bool(int.from_bytes(self.serial_buffer_packet[0:1], byteorder='big') & 0x08)

        proximity = bool(int.from_bytes(self.serial_buffer_packet[0:1], byteorder='big') & 0x40)

        button = int.from_bytes(self.serial_buffer_packet[3:4], byteorder='big') >> 3 if button_pressed else 0

        self.set_position(pos_x, pos_y)
        self.set_pressure(pressure)
        #self.set_tilt(tilt_x, tilt_y)
        self.proximity = proximity
        self.press = button == 1

        send_report_packet_to_driver(self)
        if (DEBUG_PRINTING):
            print(f'pos_x: {pos_x:5d}, pos_y: {pos_y:5d}, proximity: {proximity:>1}, button: {button:2d}, pressure: {pressure:3d}', end='\r')

    def read_input_data(self):
        bytes_to_read = self.serial_port.in_waiting

        # check if there are any bytes to read from the serial port and load
        # them into the main buffer one by one
        if bytes_to_read:
            read_bytes = self.serial_port.read(bytes_to_read)
            for i in range(len(read_bytes)):
                self.serial_buffer[self.serial_buffer_write_index % len(self.serial_buffer)] = read_bytes[i]
                self.serial_buffer_write_index = self.serial_buffer_write_index + 1

        while self.serial_buffer_read_index < self.serial_buffer_write_index:
            temp_index = self.serial_buffer_read_index % len(self.serial_buffer)

            # we increment this here so that we can maintain the current read
            # index if we break out of this loop early
            self.serial_buffer_read_index = self.serial_buffer_read_index + 1

            # if we encounter a sync bit, then reset the buffer packet index back
            # to zero, regardless if the packet we were building was ever parsed,
            # since if we encounter this earlier than expected then it could be
            # indicative of a corrupted packet.
            if int.from_bytes(self.serial_buffer[temp_index:temp_index+1], byteorder='big') & 0x80:
                if self.serial_buffer_packet_index < 7:
                    if (DEBUG_PRINTING):
                        print('dropped packet!')
                self.serial_buffer_packet_index = 0

            # load bytes into packet to read from, ignoring the rest until the
            # next syc bit arrives
            if self.serial_buffer_packet_index < 7:
                self.serial_buffer_packet[self.serial_buffer_packet_index] = self.serial_buffer[temp_index]
                self.serial_buffer_packet_index = self.serial_buffer_packet_index + 1

                # parse the packet once it has been fully loaded and break out of
                # the loop since we only want to update our position once per main
                # iteration of the main loop
                if self.serial_buffer_packet_index == 7:
                    self.parse_wacom_iv_packet()

def send_report_packet_to_driver(tablet):
    report_buffer = [0xFF]*65
    button_flags = 0  # bitwise
    scaled_pressure = 0

    button_flags = set_bit(button_flags, 0) if tablet.press else unset_bit(button_flags, 0)
    button_flags = set_bit(button_flags, 4) if tablet.proximity else unset_bit(button_flags, 4)
    scaled_pressure = tablet.pressure * 32
    report_buffer[0] = VIRTUAL_MULTITOUCH_ID
    report_buffer[1] = 12
    report_buffer[2] = VIRTUAL_MULTITOUCH_REPORT_ID_WINDOWSINK
    report_buffer[3] = button_flags  # button bits

    scaled_pos_x = int(((32767 / TABLET_MAX_X_POS) * tablet.pos_x) * ((MAPPED_MONITOR_RES_X + OFFSET_X) / ALL_MONITORS_RES_X)) # scales x pos for vmulti, 32767 is the max pos value for vmulti
    report_buffer[4] = scaled_pos_x & 0xFF  # lower 8 bits of X value
    report_buffer[5] = (scaled_pos_x & 0xFF00) >> 8  # upper 8 bits of X value

    scaled_pos_y = int((32767 / TABLET_MAX_Y_POS) * tablet.pos_y * ((MAPPED_MONITOR_RES_Y + OFFSET_Y) / ALL_MONITORS_RES_Y)) # scales y pos for vmulti, 32767 is the max pos value for vmulti
    report_buffer[6] = scaled_pos_y & 0xFF  # lower 8 bits of Y value
    report_buffer[7] = (scaled_pos_y & 0xFF00) >> 8  # upper 8 bits of Y value

    report_buffer[8] = scaled_pressure & 0xFF  # lower 8 bits of pressure
    report_buffer[9] = (scaled_pressure & 0xFF00) >> 8  # upper 8 bits of pressure

    #report_buffer[10] = tablet.tilt_x * 2  # tilt x
    #report_buffer[11] = tablet.tilt_y * 2  # tilt y
    report.set_raw_data(report_buffer)
    report.send()

virtual_device = None
report = None

# Product and Vendor ID should correspond to the Virtual Multitouch Device driver
all_devices = hid.HidDeviceFilter(
    vendor_id=VIRTUAL_MULTITOUCH_DEVICE_VENDOR_ID,
    product_id=VIRTUAL_MULTITOUCH_DEVICE_PRODUCT_ID,
).get_devices()

if len(all_devices) > 0:
    virtual_device = all_devices[-1]
    if (DEBUG_PRINTING):
        print(f'Found HID driver: {virtual_device.vendor_name} {virtual_device.product_name} (vID=0x{virtual_device.vendor_id:04x}, pID=0x{virtual_device.product_id:04x})')
else:
    sys.exit("Virtual Multitouch Device driver not loaded.")

try:
    virtual_device.open()
    serial_port = serial.Serial(
        port="COM3",
        baudrate=9600,
        bytesize=8,
        timeout=2,
        stopbits=serial.STOPBITS_ONE,

    )

    tablet = WacomSerialTablet(serial_port)

    reports = virtual_device.find_output_reports()
    report = reports[-1]

    while(1):
        tablet.read_input_data()
        #time.sleep(0.01)

finally:
    serial_port.close()
    virtual_device.close()
