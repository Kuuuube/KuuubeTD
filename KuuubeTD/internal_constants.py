import user_constants

#general tablet specs
WACOM_IVE_1_4_MAX_PRESSURE = 256
WACOM_IV_1_2_TO_1_4_MAX_PRESSURE = 256
WACOM_IV_1_0_TO_1_1_MAX_PRESSURE = 128
WACOM_II_S_MAX_PRESSURE = 64

WACOM_IVE_1_4_MAX_TILT = 64

#vmulti
VMULTI_DEVICE_VENDOR_ID = 0x00FF
VMULTI_DEVICE_PRODUCT_ID = 0xBACC
VMULTI_ID = 0x40
VMULTI_REPORT_ID_DIGITIZER = 0x05
VMULTI_REPORT_ID_MOUSE = 0x09
USAGE_PAGE_DIGITIZER = 0x0D

OUTPUT_MODE = VMULTI_REPORT_ID_DIGITIZER #VMULTI_REPORT_ID_DIGITIZER or VMULTI_REPORT_ID_MOUSE

VMULTI_MONITOR_SCALING_X = (32767 / user_constants.TABLET_MAX_X_POS) * (user_constants.MAPPED_MONITOR_RES_X / user_constants.ALL_MONITORS_RES_X)
VMULTI_MONITOR_SCALING_Y = (32767 / user_constants.TABLET_MAX_Y_POS) * (user_constants.MAPPED_MONITOR_RES_Y / user_constants.ALL_MONITORS_RES_Y)

VMULTI_MONITOR_OFFSET_X = 32767 * (user_constants.MONITOR_OFFSET_X / user_constants.ALL_MONITORS_RES_X)
VMULTI_MONITOR_OFFSET_Y = 32767 * (user_constants.MONITOR_OFFSET_Y / user_constants.ALL_MONITORS_RES_Y)

VMULTI_MONITOR_RES_X = user_constants.MAPPED_MONITOR_RES_X * (32767 / user_constants.MAPPED_MONITOR_RES_X)
VMULTI_MONITOR_RES_Y = user_constants.MAPPED_MONITOR_RES_Y * (32767 / user_constants.MAPPED_MONITOR_RES_Y)

VMULTI_PRESSURE_SCALING_WACOM_IVE_1_4 = 8192 / WACOM_IVE_1_4_MAX_PRESSURE
VMULTI_PRESSURE_SCALING_WACOM_IV_1_2_TO_1_4 = 8192 / WACOM_IV_1_2_TO_1_4_MAX_PRESSURE
VMULTI_PRESSURE_SCALING_WACOM_IV_1_0_TO_1_1 = 8192 / WACOM_IV_1_0_TO_1_1_MAX_PRESSURE
VMULTI_PRESSURE_SCALING_WACOM_II_S = 8192 / WACOM_II_S_MAX_PRESSURE

VMULTI_TILT_SCALING_WACOM_IVE_1_4 = 128 / WACOM_IVE_1_4_MAX_TILT

#serial port
SERIAL_PORT_INITIAL_BAUD_RATE = 9600
SERIAL_PORT_FINAL_BAUD_RATE = 19200
SERIAL_PORT_BYTESIZE = 8
SERIAL_PORT_TIMEOUT = 1
SERIAL_PORT_STOPBITS = 1

SERIAL_PORT_WACOM_IVE_1_4_REPORT_SIZE = 9
SERIAL_PORT_WACOM_IV_1_2_TO_1_4_REPORT_SIZE = 7
SERIAL_PORT_WACOM_IV_1_0_TO_1_1_REPORT_SIZE = 7
SERIAL_PORT_WACOM_II_S_REPORT_SIZE = 7

#wacom serial port commands
GLOBAL_RESET_TO_WACOM_IV_COMMAND = "#"
WACOM_IVE_1_4_SETTINGS_COMMAND = "~*F233C910,000,00,2540,2540"
WACOM_IV_1_2_TO_1_4_SETTINGS_COMMAND = "~*F233C900,000,00,2540,2540"
WACOM_IV_1_0_TO_1_1_SETTINGS_COMMAND = "~*F233C900,000,00,1270,1270"
WACOM_II_S_RESET_COMMAND = "RE"
WACOM_II_S_PRESSURE_MODE_COMMAND = "PH1"
WACOM_II_S_BINARY_MODE_COMMAND = "AS1"
WACOM_II_S_INCREMENT_COMMAND = "IN0"
WACOM_II_S_OPERATION_MODE_COMMAND = "SR"
