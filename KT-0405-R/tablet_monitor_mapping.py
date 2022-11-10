import constants

def map_x(pos_x):
    return int(clamp((constants.VMULTI_MONITOR_SCALING_X * (pos_x - constants.TABLET_OFFSET_X) + constants.VMULTI_MONITOR_OFFSET_X), constants.VMULTI_MONITOR_OFFSET_X, constants.VMULTI_MONITOR_OFFSET_X + constants.VMULTI_MONITOR_RES_X))

def map_y(pos_y):
    return int(clamp((constants.VMULTI_MONITOR_SCALING_Y * (pos_y - constants.TABLET_OFFSET_Y) + constants.VMULTI_MONITOR_OFFSET_Y), constants.VMULTI_MONITOR_OFFSET_Y, constants.VMULTI_MONITOR_OFFSET_Y + constants.VMULTI_MONITOR_RES_Y))

def clamp(input, minimum, maximum):
    return max(min(input, maximum), minimum)