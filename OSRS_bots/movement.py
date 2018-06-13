import pyautogui
import time
import numpy
import random
import cv2
from track import track
import math


def main():
	bezier4(222,134)



def bezier4(x4,y4):
	loc = pyautogui.position()


	x1 = loc[0]
	y1 = loc[1]

	x4 = x4
	y4 = y4

	x2 = (x4-x1)/2
	y2 = y1

	x3 = x2
	y3 = y4

	t = 0
	while(t<=1):
		x = math.pow((1-t),3)*x1 + 3*math.pow((1-t),2)*t*x2 + 3*(1-t)*math.pow(t,2)*x3 + math.pow(t,3)*x4
		y = math.pow((1-t),3)*y1 + 3*math.pow((1-t),2)*t*y2 + 3*(1-t)*math.pow(t,2)*y3 + math.pow(t,3)*y4
	
		pyautogui.moveTo(x,y)
		t+=0.2

def bezier3(x3,y3):
	loc = pyautogui.position()

	x1=loc[0]
	y1=loc[1]
	x3=x3
	y3=y3
	x2=x3
	y2= (y3+y1)/2
	t = 0
	
	while(t<=1):
		x = math.pow((1-t), 2)*x1 + 2*(1-t)*t*x2 + math.pow(t,2)*x3
		y = math.pow((1-t), 2)*y1 + 2*(1-t)*t*y2 + math.pow(t,2)*y3

		
		pyautogui.moveTo(x,y, duration=.05)
		t+=0.2





if __name__ == '__main__':
	main()


