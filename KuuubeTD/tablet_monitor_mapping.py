from internal_constants import *
from user_constants import *

def map_x(pos_x):
    return int(clamp((VMULTI_MONITOR_SCALING_X * (pos_x - TABLET_OFFSET_X) + VMULTI_MONITOR_OFFSET_X), VMULTI_MONITOR_OFFSET_X, VMULTI_MONITOR_OFFSET_X + VMULTI_MONITOR_RES_X))

def map_y(pos_y):
    return int(clamp((VMULTI_MONITOR_SCALING_Y * (pos_y - TABLET_OFFSET_Y) + VMULTI_MONITOR_OFFSET_Y), VMULTI_MONITOR_OFFSET_Y, VMULTI_MONITOR_OFFSET_Y + VMULTI_MONITOR_RES_Y))

def clamp(input, minimum, maximum):
    return max(min(input, maximum), minimum)