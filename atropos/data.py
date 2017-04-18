#!/usr/bin/env python

"""readin for serial data from LightBlue Bean as a preamble to converting data to text"""

import time
import serial

ser = serial.Serial('/dev/cu.LightBlue-Bean', 57600)


while True:
    message = ser.readline()
    print((message).decode())
    output_text = ((message).decode())

    # Write the status to a file, for logging
    with open('txtout/data.txt', 'a') as f:
        f.write(output_text + '\n')
    time.sleep(1)
