#first bot
import pyautogui
import time
import random
import sys
from login import login
from track import track
from drop import dropAll
from movement import bezier3
from movement import bezier4
from password import get_pwd
import sand


def toggleRun():
	pass

def pos():
	while(1):
		print(pyautogui.position())
		time.sleep(1)

def test():
	sand.F_reset()




def sandc():
	sand.sand()

	

def fruit():
	randxy_move(998,525,1002,532)
	loop=0
	while 1:
		if loop % 28 == 0 and loop!=0:
			dropAll()
			randxy_move(999,515,1009,530)
		pyautogui.click()
		time.sleep(3.1 + random.random())
		loop+=1
		if loop%840 == 0:
			logback(300 + random.randint(0,60))






def alch():
	countdown(5)
	#move to random  range of spellbook
	randxy_move(1896,724,1900,729)
	wait(0.2,0.5)
	pyautogui.click()
	time.sleep(0.2)
	randxy_move(1868,868,1873,870)
	loop=0

	while(1):
		pyautogui.click()
		time.sleep(1.5+random.random())
		loop+=1
		if(loop%200 ==0 or loop%32 == 0 or loop%167 ==0):
			randxy_move(1868,868,1873,870)
			wait(0.8,1.4)
			loop+=1
		if(loop % 1000 ==0):
			off = random.randint(300,900)
			logback(off)
			loop+=1
			randxy_move(1896,724,1900,729)
			wait(0.2,0.5)
			pyautogui.click()
			time.sleep(0.2)
			randxy_move(1868,868,1873,870)
		

		
	


	

def mine():


	loop=0
	x= random.randint(962,968)
	y= random.randint(479,481)

	x2 = random.randint(1000,1007)
	y2 = random.randint(522,527)

	while(1):
		randxy_move(962,479,968,481)
		pyautogui.click()
		time.sleep(2.5)
		randxy_move(1000,522,1007,527)
		pyautogui.click()
		time.sleep(4.75 + random.random())
		loop+=1

		if loop % 14 == 0:
			dropAll()
			
		if(loop%270 == 0):
			logback(random.randint(40,120))

			





'''
	for rock in rocks:
		move cursor over rock
		check/wait if mineable
		click
		wait to finish mining
		wait some random time
		move to next rock
'''

def bank():
	pass

def login():
	login.login("redacted")


	'''
	for bank in banks:
		move cursor over a booth
		click
		wait random time
		move back to start
		'''	

def resetCamera():
	loc = pyautogui.position()
	randxy_move(1755,33,1760,43)
	time.sleep(.18)
	pyautogui.click()
	start = time.time()
	while time.time() - start < 4 + random.randint(1,10)/10:
		pyautogui.keyDown('up')
	time.sleep(.2)
	bezier3(loc[0],loc[1])

def countdown(dur):
	i =0
	print("starting")
	while i<dur:
		print("in ", i)
		i+=1
		time.sleep(1)



def randxy_move(x_min,y_min,x_max,y_max):

	x = random.randint(x_min, x_max)
	y = random.randint(y_min, y_max)
	#print("move to",x,y)
	return bezier3(x, y)

def wait(min,max):

	min=min
	max=max

	if min>1:
		t=random.random() + random.randint(min,max)
	else:
		t = random.random()
	previous_loc = pyautogui.position()


	if(t>=10):
		randxy_move(3312,537,3380,625)
		#pyautogui.click()
		time.sleep(t)
		randxy_move(1802,1807,720,725)
		pyautogui.click()
		bezier3(previous_loc[0],previous_loc[1])

	else:
		time.sleep(t)


def logback(duration):
	loc = pyautogui.position()
	#goto and click door
	randxy_move(1797,1010,1801,1018)
	pyautogui.click()
	time.sleep(.1)
	pyautogui.click()
	#goto and click logout
	randxy_move(1790,965,1810,970)
	time.sleep(.12)
	pyautogui.click()
	time.sleep(10)
	pyautogui.click()
	print("logged out")
	print(time.time())
	#wait
	time.sleep(duration)
	randxy_move(998,305,1023,311)
	time.sleep(.124)
	pyautogui.click()
	#write pwd
	username = "redacted"
	password = get_pwd(username)
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
	pyautogui.typewrite(['enter'])
	time.sleep(4)
	randxy_move(964,344,1000,373)
	time.sleep(.1)
	pyautogui.click()
	bezier3(loc[0],loc[1])
	print("back online")
	print(time.time())







def main():
	#set_user
	username = "redacted"
	password = get_pwd(username)
	pyautogui.FAILSAFE = True

	if(len(sys.argv) > 1):
		script = sys.argv[1]
	else:
		script = "test"

	if script == "test":
		print("running test: ")
		test()

	elif script == "login":
		print("logging in: ")
		login()
	elif script == "pos":
		print("logging position: ")
		pos()
	elif script == "mine":
		print("running mine: ")
		mine()

	elif script == "alch":
		print("running alch: ")
		alch()
	elif script == "fruit":
		print("stealing fruit: ")
		fruit()
	elif script == "sandc":
		print("sandcrabbing")
		sand.sand()
	elif script == "sand2":
		print("sandcrabbing2")
		sand.sand2()
	



if __name__ == '__main__':
	main()