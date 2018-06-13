#drop bot
import random
from movement import bezier3,bezier4
import pyautogui
import time
import math

def main():
	dropAll()


def dropAll():
	inventory = genInventory()
	#select inventory
	bezier3(1802 + random.randint(1,3) ,720 + random.randint(1,3))
	time.sleep(1 + random.random()/5)
	pyautogui.click()
	time.sleep(0.5 + random.random()/5)
	h = inventory[0]
	bezier3(h[0],h[1])

	time.sleep(1)
	for spot in inventory:
		time.sleep(random.randint(1,25)/125)

		bezier3(spot[0],spot[1])
		pyautogui.keyDown('shift')
		pyautogui.click()
		#time.sleep(random.randint(1,2)/10)
		pyautogui.keyUp('shift')




def genInventory():

	inventory = []

	inventory.append((1737 + random.randint(0,4), 762 + random.randint(0,3)))
	inventory.append((1780 + random.randint(0,4), 762 + random.randint(0,3)))
	inventory.append((1822 + random.randint(0,4), 762 + random.randint(0,3)))
	inventory.append((1861 + random.randint(0,4), 762 + random.randint(0,3)))

	inventory.append((1861 + random.randint(0,4), 800 + random.randint(0,3)))
	inventory.append((1822 + random.randint(0,4), 800 + random.randint(0,3)))
	inventory.append((1780 + random.randint(0,4), 800 + random.randint(0,3)))
	inventory.append((1737 + random.randint(0,4), 800 + random.randint(0,3)))
		
	inventory.append((1737 + random.randint(0,4), 840 + random.randint(0,3)))
	inventory.append((1780 + random.randint(0,4), 840 + random.randint(0,3)))
	inventory.append((1822 + random.randint(0,4), 840 + random.randint(0,3)))
	inventory.append((1861 + random.randint(0,4), 840 + random.randint(0,3)))

	inventory.append((1861 + random.randint(0,4), 880 + random.randint(0,3)))
	inventory.append((1822 + random.randint(0,4), 880 + random.randint(0,3)))
	inventory.append((1780 + random.randint(0,4), 880 + random.randint(0,3)))
	inventory.append((1737 + random.randint(0,4), 880 + random.randint(0,3)))
		
	inventory.append((1737 + random.randint(0,4), 920 + random.randint(0,3)))
	inventory.append((1780 + random.randint(0,4), 920 + random.randint(0,3)))
	inventory.append((1822 + random.randint(0,4), 920 + random.randint(0,3)))
	inventory.append((1861 + random.randint(0,4), 920 + random.randint(0,3)))

	inventory.append((1861 + random.randint(0,4), 955 + random.randint(0,3)))
	inventory.append((1822 + random.randint(0,4), 955 + random.randint(0,3)))
	inventory.append((1780 + random.randint(0,4), 955 + random.randint(0,3)))
	inventory.append((1737 + random.randint(0,4), 955 + random.randint(0,3)))
		
	inventory.append((1737 + random.randint(0,4), 993 + random.randint(0,3)))
	inventory.append((1780 + random.randint(0,4), 993 + random.randint(0,3)))
	inventory.append((1822 + random.randint(0,4), 993 + random.randint(0,3)))
	inventory.append((1861 + random.randint(0,4), 993 + random.randint(0,3)))

	return inventory

	


	




if __name__ == '__main__':
	main()