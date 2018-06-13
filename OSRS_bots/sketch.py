import pyautogui
import time
import random
import sys
import cv2
import numpy as np
from scipy.interpolate import spline, UnivariateSpline, Akima1DInterpolator, PchipInterpolator
from track import track
import matplotlib.pyplot as plt




def main():
	'''
	print("Tracking in:")
	print("5")
	time.sleep(1)
	print("4")
	time.sleep(1)
	print("3")
	time.sleep(1)
	print("2")
	'''
	time.sleep(1)
	print("1")
	time.sleep(1)
	print("Start!")


	path = track(5)
	Ax_data= []
	Ay_data= []
	rep = 0
	for entry in path:
		if rep > 0:
			Ax_data.append(abs(float(entry[0])))
			Ay_data.append(abs(float(entry[1])))
			rep+=1
		if rep == 0:
			rep=1


	x_data = np.array(Ax_data)
	y_data = np.array(Ay_data)


	x_data_smooth = np.linspace(min(x_data), max(x_data), 1000)

	fig, ax = plt.subplots(1,1)

	spl = UnivariateSpline(x_data, y_data, s=0, k=2)
	y_data_smooth = spl(x_data_smooth)
	ax.plot(x_data_smooth, y_data_smooth, 'b')

	bi = Akima1DInterpolator(x_data, y_data)
	y_data_smooth = bi(x_data_smooth)
	ax.plot(x_data_smooth, y_data_smooth, 'g')

	bi = PchipInterpolator(x_data, y_data)
	y_data_smooth = bi(x_data_smooth)
	ax.plot(x_data_smooth, y_data_smooth, 'k')

	ax.plot(x_data_smooth, y_data_smooth)
	ax.scatter(x_data, y_data)

	plt.show()





if __name__ == '__main__':
	main()
