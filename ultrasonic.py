#!/usr/bin/env python3

import gpiozero


sensor1 = gpiozero.DistanceSensor(echo=20,trigger=21)
sensor2 = gpiozero.DistanceSensor(echo=17,trigger=27)


for j in range(100):
    print('S1 Distance: ', sensor1.distance * 100)
    print('S2 Distance: ', sensor2.distance * 100)
    time.sleep(0.1)
