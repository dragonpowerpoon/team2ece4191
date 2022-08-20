#!/usr/bin/env python3

import gpiozero
import time
from multiprocessing import Process
import os
def printEncoder():
	while True:
		print(2)
		time.sleep(0.1)



def motorController():
	while True:
		print(1)
		time.sleep(0.1)

if __name__ == '__main__':
	p = Process(target=motorController)
	p.start()
	k = Process(target = printEncoder)
	k.start()
	p.join() 