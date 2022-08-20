#!/usr/bin/env python3
import gpiozero
import time
import asyncio
from concurrent.futures import ProcessPoolExecutor

async def motorcontrol():
    pwm = gpiozero.PWMOutputDevice(pin=12,active_high=True,initial_value=0,frequency=100)
    in1F = gpiozero.OutputDevice(pin=5)
    in2B = gpiozero.OutputDevice(pin=6)
    standby = gpiozero.OutputDevice(pin=26)
    encoderinput1 = gpiozero.InputDevice(pin=17)
    in1F.on()
    in2B.off()
    standby.on()
    pwm.value = 0.8
    #encoder = gpiozero.RotaryEncoder(a=21, b=20,max_steps=100000) 
    # This class has a lot more functionality,so worth reading up on it

    # Step through duty cycle values, slowly increasing the speed and changing the direction of motion
    #encoder.steps = 0
    while True:
        print(encoderinput1.value)
        time.sleep(0.001)





if __name__ == "__main__":
    asyncio.run(motorcontrol())





#for j in range(10):
#    pwm.value = j/10
#    dir1.value = not dir1.value
#   dir2.value = not dir1.value
#    print('Duty cycle:',pwm.value,'Direction:',dir1.value)
#    time.sleep(5.0)
#    print('Counter:',encoder.steps,'Speed:',(encoder.steps)/5.0,'steps per second\n')
#    encoder.steps = 0

#pwm.value =0 




