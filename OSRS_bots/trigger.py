#check for triggers
import time
import pyautogui
import cv2
import random
import numpy

def wait_to_get_triggered():
	r = triggers[0], triggers[1], triggers[2], triggers[3]
	img = triggers[4]
	while image_match(r,img) == False:
		print("images don't match!")
		time.sleep(3)


def image_match(r, img):
	pyautogui.screenshot('trigger_shots/screenshot.png', region = r)
	my_screen = cv2.imread('trigger_shots/screenshot.png')

