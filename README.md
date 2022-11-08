# Serial Wacom Tools

### Proper documentation will be added soon.

`KT-0405-R/KT_0405_R_driver.py` has been tested only on KT-0405-R with rom version 1.3-2. To find your tablet's rom version run `wacom_serial_tablet_diagnostics.py`.

Install vmulti from `vmulti_driver.zip`. (Extract and run `install_hiddriver.bat` as admin)

For proper monitor mapping change the following variables in `constants.py` to what they should be for your setup: `ALL_MONITORS_RES_X`, `ALL_MONITORS_RES_Y`, `MAPPED_MONITOR_RES_X`, `MAPPED_MONITOR_RES_Y`, `OFFSET_X`, `OFFSET_Y`. 

You may also need to change `TABLET_MAX_X_POS` and `TABLET_MAX_Y_POS` if your tablet does not use the same resolution as mine.

Custom tablet areas are not yet supported. You can somewhat add a custom area by changing `TABLET_MAX_X_POS` and `TABLET_MAX_Y_POS` to be lower than the actual maxes.

