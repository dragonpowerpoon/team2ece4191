#!/usr/bin/env python3

import gpiozero
import time

sensor = gpiozero.DistanceSensor(echo=20,trigger=21)

for j in range(100):
    print('Distance: ', sensor.distance * 100)
    time.sleep(0.1)
