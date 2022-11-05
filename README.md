# Serial Wacom Tools

## Proper documentation will be added soon.

`serial_driver_with_win_ink_KT-0405-R.py` has been tested only on KT-0405-R with rom version 1.3-2.

For proper monitor mapping change the following variables to what they should be for your setup: `ALL_MONITORS_RES_X`, `ALL_MONITORS_RES_Y`, `MAPPED_MONITOR_RES_X`, `MAPPED_MONITOR_RES_Y`, `OFFSET_X`, `OFFSET_Y`. 

You may also need to change `TABLET_MAX_X_POS` and `TABLET_MAX_Y_POS` if your tablet does not use the same resolution as mine. Change `DEBUG_PRINTING` to `True` so you can see what the position values are reporting as.

Custom tablet areas are not yet supported. You can somewhat add a custom area by changing `TABLET_MAX_X_POS` and `TABLET_MAX_Y_POS` to be lower than the actual maxes.

If your tablet follows similar specifications but does not work with this driver you can change `DEBUG_PRINTING` to `True` then run the driver to check what your tablet reports as.