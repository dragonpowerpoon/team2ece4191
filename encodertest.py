#!/usr/bin/env python3

import gpiozero
import time
from multiprocessing import Process
import os


def printEncoder():
	lEncoder = gpiozero.RotaryEncoder(a=19, b=16,max_steps=100000)
	rEncoder = gpiozero.RotaryEncoder(a=23, b=24,max_steps=100000)
	lprevious = 0
	rprevious = 0
	while True:

		lSteps = lEncoder.steps
		rSteps = rEncoder.steps
		lSpeed = lSteps - lprevious
		rSpeed = rSteps - rprevious
		print("Left", lSpeed, "Right", rSpeed)
		lprevious = lSteps
		rprevious = rSteps
		time.sleep(0.1)

	#encoderinput1 = gpiozero.InputDevice(pin=19)
	#encoderinput2 = gpiozero.InputDevice(pin=16)
	#prevEncoderVal = 0
	#prevTime = 0
	#while True:
	#	currEncoderVal = encoderinput1.value
	#	if prevEncoderVal == 0 and encoderinput1.is_active:
	#		currTime = time.perf_counter()
	#		freq = 1/(currTime - prevTime)
	#		prevTime = currTime
	#		print(freq)
	#	prevEncoderVal = currEncoderVal
	#
	#	time.sleep (0.0002)

def motorController():
	pwm  = gpiozero.PWMOutputDevice(pin=12,active_high=True,initial_value=0,frequency=100)
	forwardDir = gpiozero.OutputDevice(pin=5)
	backwardDir = gpiozero.OutputDevice(pin=6)
	standby = gpiozero.OutputDevice(pin=26)

	standby.on()
	run = True
	forwardDir.off()
	backwardDir.on()
	pwm.value = 0
	
	while run == True:
		#directionFlag = input("set motor direction (b/f): ")
		directionFlag = "b"
		if directionFlag == "b":
			#forwardDir.off()
			backwardDir.on()
		elif directionFlag == "f":
			forwardDir.on()
			backwardDir.off()
		else:
			run = False
			print('direction input invalid')

		#speedFlag = float(input("set speed (0-100): "))
		speedFlag =  40
		if speedFlag <= 100:
			pwm.value = speedFlag/100
		else:
			run = False
			print('Error: PWM value invalid')

		#print('direction: ', directionFlag, 'Speed:', pwm.value, '\n')
		time.sleep (0.01)

if __name__ == '__main__':
	p = Process(target=motorController)
	p.start()
	k = Process(target = printEncoder)
	k.start()
	p.join()