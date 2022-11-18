# FAQ

### 1. Why is windows the only supported OS?

It is what I am most familiar with and could easily implement. The only windows specific part of this driver is the use of vmulti. Replacing `vmulti_handler.py` with something which can send data on another OS would allow is to work there as well.

### 2. Why would you code a driver in python? Won't python be slow or add a lot of overhead?

I couldn't get standard libraries in other languages to read off of my serial to usb adapter when I started this project. It may be rewritten in the future.

There are no issues with latency, all calculations and data are sent in less than a milisecond from being received. The tablets supported by this driver max out at 205 rps which means at most they will send one report every 4.87ms. Due to the use of blocking reads the overhead is extremely small.

### 3. Misc

If you have any questions about this driver or tablets in general, feel free to join the [Discord Server](https://discord.gg/T5vEAh4ruF) and ask.