import pyautogui
import time
import numpy
import random
import cv2



def pos():
	while(1):
		print(pyautogui.position())
		time.sleep(0.5)

def track():
	fh = open("mouse_data.txt", "w")
	while(1):
		write(gen_mouseInstance)
		time.sleep(0.2)
	fh.close()



class mouseInstance(object):
    x = 0
    y = 0
    time = time.time()

def gen_mouseInstance():
	instance = mouseInstance()
	coord = pyautogui.position()
	time = time.time()
	instance.x = coord[0]
	instance.y = coord[1]

	return instance


def main():
	track()


		
