import time
import pyautogui


def main():
	num=0
	while (1):
		print("SCREENSHOT: ", float(time.time()))
		pyautogui.screenshot('tracking/screenshot' + str(num) + '.png')
		time.sleep(10)
		num+=1


if __name__ == '__main__':
	main()