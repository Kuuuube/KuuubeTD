# General Usage

- Install vmulti from `vmulti/vmulti_driver.zip`. (Extract and run `install_hiddriver.bat` as admin.)

- Change `SERIAL_PORT_PATH` in `KuuubeTD/user_constants.py` to the path the tablet is connected to.

    If you are unsure which path to use, run `tools/find_serial_port_paths.py`. (You may have to guess between a few if there are multiple options.)

- For proper monitor mapping, change the following variables in `KuuubeTD/user_constants.py` to the correct values for your setup: 

    `ALL_MONITORS_RES_X`: This is the X axis resolution of all your monitors combined. 
    
    For example, two 1920 x 1080 monitors positioned side by side have an `ALL_MONITORS_RES_X` of 3840, and two 1920 x 1080 monitors positioned up and down have an `ALL_MONITORS_RES_X` of 1080.

    `ALL_MONITORS_RES_Y`: This is the Y axis resolution of all your monitors combined. 
    
    For example, two 1920 x 1080 monitors positioned side by side have an `ALL_MONITORS_RES_Y` of 1080, and two 1920 x 1080 monitors positioned up and down have an `ALL_MONITORS_RES_Y` of 2160.

    `MAPPED_MONITOR_RES_X`: This is the X axis resolution of the monitor mapping to apply. 
    
    For example, to map to a 1920 x 1080 monitor, the `MAPPED_MONITOR_RES_X` will be 1920 regardless of how many monitors you have.

    `MAPPED_MONITOR_RES_Y`: This is the Y axis resolution of the monitor mapping to apply. 
    
    For example, to map to a 1920 x 1080 monitor, the `MAPPED_MONITOR_RES_Y` will be 1080 regardless of how many monitors you have.
    
    `MONITOR_OFFSET_X`: This is the X axis offset to apply to `MAPPED_MONITOR_RES_X`. (Offsets are added from the top left corner.)

    For example, on a setup with two 1920 x 1080 monitors side by side, to map to the right monitor, `MONITOR_OFFSET_X` will be 1920, and to map to the left monitor, `MONITOR_OFFSET_X` will be 0.
    
    `MONITOR_OFFSET_Y`: This is the Y axis offset to apply to `MAPPED_MONITOR_RES_Y`. (Offsets are added from the top left corner.)

    For example, on a setup with two 1920 x 1080 monitors up and down, to map to the bottom monitor, `MONITOR_OFFSET_Y` will be 1080, and to map to the top monitor, `MONITOR_OFFSET_Y` will be 0.
    
- Optionally, to use a custom tablet area instead of full area, change the following variables in `KuuubeTD/user_constants.py` to the desired values:

    `TABLET_MAX_X_POS`: The tablet area width in tablet coordinates to use for the size of the tablet area.

    `TABLET_MAX_Y_POS`: The tablet area height in tablet coordinates to use for the size of the tablet area.

    `TABLET_OFFSET_X`: The X axis offset to apply to `TABLET_MAX_X_POS` in tablet coordinates to change the position of the tablet area. (Offsets are added from the top left corner.)

    `TABLET_OFFSET_Y`: The Y axis offset to apply to `TABLET_MAX_Y_POS` in tablet coordinates to change the position of the tablet area. (Offsets are added from the top left corner.)