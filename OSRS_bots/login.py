#bot login
import pyautogui
import time
import random
import sys
import cv2
import numpy
from password import get_pwd


#logs in to the client on my monitor

def hold_back (hold_time):
    start = time.time()
    while time.time() - start < hold_time:
        pyautogui.keyDown('backspace')

def login(username):
	username = username
	password = "redacted"
	#minimize windows
	pyautogui.hotkey('win', 'm')
	pyautogui.moveTo(168, 1057, duration=0.25)
	pyautogui.click(button='left')
	time.sleep(10)
	#maximize rs
	pyautogui.moveTo(1300, 150, duration=0.1)
	pyautogui.click(button='left')
	#enter login screen
	time.sleep(0.5)
	pyautogui.typewrite(['enter'])
	time.sleep(0.5)

	#select UN
	pyautogui.moveTo(1046, 292, duration=0.5)
	pyautogui.click(button='left')
	#delete UN
	hold_back(4)
	#write UN
	timeU=[]
	for c in username:
		r = random.randint(5,30)
		d = random.randint(1,3)
		e = random.randint(1,6)/100
		timeU.append((r/d)*e/2)
	rep = 0
	for c in username:
		time.sleep(timeU[rep])
		pyautogui.typewrite(c)
		rep+=1

	#select PWD
	pyautogui.typewrite(['tab'])
	#write PWD
	timeP=[]
	for c in password:
		r = random.randint(5,30)
		d = random.randint(1,3)
		e = random.randint(1,6)/100
		timeP.append((r/d)*e/3)
	rep = 0
	for c in password:
		time.sleep(timeP[rep])
		pyautogui.typewrite(c)
		rep+=1

	#select world
	pyautogui.moveTo(630, 520, duration=0.5)
	pyautogui.click(button='left')
	#sort free
	pyautogui.moveTo(1210, 57, duration=0.9)
	pyautogui.click(button='left')
	#world 308
	pyautogui.moveTo(777, 114, duration=0.7)
	pyautogui.click(button='left')
	#Select LOGIN button
	pyautogui.moveTo(888, 365, duration=0.4)
	pyautogui.click(button='left')
	time.sleep(5)
	pyautogui.click(button='left')











def randxy_move(x_min,y_min,x_max,y_max):

	x = random.randint(x_min, x_max)
	y = random.randint(y_min, y_max)
	print("move to",x,y)
	return bezier3(x, y)




def main():
	login()

if __name__ == '__main__':
	main()
