# Finding ROM Version

On UD and KT tablets: 

- To find your tablet's ROM, run `tools/wacom_serial_tablet_diagnostics.py`. The end of `Tablet ID` will show your ROM version. (Do not use the `Tablet Size` listed from this tool. Only use it to check the ROM version.)

- Examples:

    `Tablet ID: ~#KT-0405-R00 V1.3-2` identifies this as a KT-0405-R with a ROM version of 1.3. This tablet is `Wacom IV 1.2-1.4`.

    `Tablet ID: ~#UD-1212-R00 V1.1-0` identifies this as a UD-1212-R with a ROM version of 1.1. This tablet is `Wacom IV 1.0-1.1`.

    `Tablet ID: ~#UD-0608-R00 V1.2-1` identifies this as a UD-0608-R with a ROM version of 1.2. This tablet is `Wacom IV 1.2-1.4`.

    `Tablet ID: ~#UD-1218-R00 V1.4-3` identifies this as a UD-1218-R with a ROM version of 1.4. This tablet is `Wacom IV 1.2-1.4` or `Wacom IVe 1.4`. Either driver will work but `Wacom IV 1.2-1.4` lacks tilt support. Using `Wacom IVe 1.4` is recommended.

On SD tablets: 

- The ROM is always `Wacom II-S` or `Wacom II`. For the purposes of this driver the differences between these do not matter. Use the `Wacom II-S` driver.