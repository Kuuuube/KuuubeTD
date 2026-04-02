from internal_constants import (
    VMULTI_MONITOR_OFFSET_X,
    VMULTI_MONITOR_OFFSET_Y,
    VMULTI_MONITOR_RES_X,
    VMULTI_MONITOR_RES_Y,
    VMULTI_MONITOR_SCALING_X,
    VMULTI_MONITOR_SCALING_Y,
)
from user_constants import (
    TABLET_MAX_X_POS,
    TABLET_MAX_Y_POS,
    TABLET_OFFSET_X,
    TABLET_OFFSET_Y,
)


def map_x(pos_x: int) -> int:
    pos_x = min(pos_x, TABLET_MAX_X_POS + TABLET_OFFSET_X)
    pos_x = max(pos_x, TABLET_OFFSET_X)
    return int(clamp((VMULTI_MONITOR_SCALING_X * (pos_x - TABLET_OFFSET_X) + VMULTI_MONITOR_OFFSET_X), VMULTI_MONITOR_OFFSET_X, VMULTI_MONITOR_OFFSET_X + VMULTI_MONITOR_RES_X))

def map_y(pos_y: int) -> int:
    pos_y = min(pos_y, TABLET_MAX_Y_POS + TABLET_OFFSET_Y)
    pos_y = max(pos_y, TABLET_OFFSET_Y)
    return int(clamp((VMULTI_MONITOR_SCALING_Y * (pos_y - TABLET_OFFSET_Y) + VMULTI_MONITOR_OFFSET_Y), VMULTI_MONITOR_OFFSET_Y, VMULTI_MONITOR_OFFSET_Y + VMULTI_MONITOR_RES_Y))

def clamp(input: int, minimum: int, maximum: int) -> int:
    return max(min(input, maximum), minimum)
