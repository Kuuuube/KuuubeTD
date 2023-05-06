from internal_constants import *
from user_constants import *

def map_x(pos_x):
    if pos_x > TABLET_MAX_X_POS + TABLET_OFFSET_X:
        pos_x = TABLET_MAX_X_POS + TABLET_OFFSET_X
    if pos_x < TABLET_OFFSET_X:
        pos_x = TABLET_OFFSET_X
    return int(clamp((VMULTI_MONITOR_SCALING_X * (pos_x - TABLET_OFFSET_X) + VMULTI_MONITOR_OFFSET_X), VMULTI_MONITOR_OFFSET_X, VMULTI_MONITOR_OFFSET_X + VMULTI_MONITOR_RES_X))

def map_y(pos_y):
    if pos_y > TABLET_MAX_Y_POS + TABLET_OFFSET_Y:
        pos_y = TABLET_MAX_Y_POS + TABLET_OFFSET_Y
    if pos_y < TABLET_OFFSET_Y:
        pos_y = TABLET_OFFSET_Y
    return int(clamp((VMULTI_MONITOR_SCALING_Y * (pos_y - TABLET_OFFSET_Y) + VMULTI_MONITOR_OFFSET_Y), VMULTI_MONITOR_OFFSET_Y, VMULTI_MONITOR_OFFSET_Y + VMULTI_MONITOR_RES_Y))

def clamp(input, minimum, maximum):
    return max(min(input, maximum), minimum)