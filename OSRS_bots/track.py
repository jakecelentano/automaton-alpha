import pyautogui
import time
import numpy
import random
import cv2
import math





def track(seconds):
	file = 'mouse_data/mouse_data.txt'
	with open(file, 'w') as f:
		start = float(time.time())
		num=0
		rep=0
		previousTime = 0
		previousX = 0
		previousY = 0
		path = [("X", "Y","T", "distance", "speed" )]



		while(time.time() -start < seconds):

			#screenshots
			'''
			if (rep % 500000 == 0):
				print("SCREENSHOT: ", float(time.time())-start)
				pyautogui.screenshot('mouse_data/screenshot' + str(num) + '.png')
				num+=1
			'''

			rep+=1
			coord = pyautogui.position()
			x = coord[0]
			y = coord[1]
			distance=  math.sqrt(math.pow(x-previousX, 2) + math.pow(y-previousY,2))
			if rep == 0:
				distance=0
			previousX = x
			previousY = y
			timestamp = (float(time.time())-start)
			delta = float(timestamp) - previousTime
			previousTime = float(timestamp)
			if rep % 5 == 0:
				path.append((x,y,round(float(timestamp),3), round(distance,4), round((distance/delta), 6)))

			#OUTPUT FILE
			#ans = str(x) + "\t" + str(y) + "\t" + str(timestamp) + '\n'
			#f.write(ans)

			time.sleep(.1)
	f.close()
	return path








def main():
	print(track(5))



if __name__ == '__main__':
	main()



		
