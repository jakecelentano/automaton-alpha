from movement import bezier3
import pyautogui
import random
from bot import randxy_move
import time
from password import get_pwd


def main():
	sand()

def randxy_move(x_min,y_min,x_max,y_max):

	x = random.randint(x_min, x_max)
	y = random.randint(y_min, y_max)
	print("move to",x,y)
	return bezier3(x, y)
#switch combat type (first two inv slots)
def switch():
	pos = pyautogui.position()
	time.sleep(random.random())
	bezier3(1737 + random.randint(0,4), 762 + random.randint(0,3))
	time.sleep(random.random())
	pyautogui.click()
	time.sleep(random.random())
	bezier3(1780 + random.randint(0,4), 762 + random.randint(0,3))
	time.sleep(random.random())
	pyautogui.click()
	time.sleep(random.random())
	bezier3(position[0],position[1])
	time.sleep(.2)


def sand2():
	username = "redacted"
	password = get_pwd(username)
	loop=0
	while (1):
		loop+=1
		print("loop: ", loop)
		if loop%7 == 0:
			logback(random.randint(60,300))
		if loop%22 == 0:
			logback(random.randint(600,1800))
		AG()
		x=0
		while (x<10):
			GI()
			IH()
			HG()
			x+=1
		GE()
		EF()
		F_reset()
		FE()
		EA()
		AB()
		x=0
		while (x<12):
			BC()
			CB()
			x+=1
		BA()			










def sand():
	username = "redacted"
	password = get_pwd(username)
	#start on starfish, south of farming patch (A)
	#time needed for a kill
	#ACTIVE ROCK SPOTS:
	# B, C, G, H, I
	AB()
	loop=0
	print("loop#: ", loop)
	while(1):
		BC()
		CB()
		loop+=1
		if loop==0:
			BFB()
		if loop%1==0 or loop==0:
			BF()
			F_reset()
			FE()
			EG()
			GHkills = 0
			while(GHkills<20):
				GI()
				GHkills+=1
				IH()
				GHkills+=1
				HG()
				GHkills+=1
			GA()
			AB()
		if loop % 50 == 0:
			if loop % 250 == 0:
				logback(random.randint(1800,3600))
			else:
				logback(random.randint(300,1200))


#re aggro B-crabs
def BFB():
	print("B => F out n back")
	BA()
	AD()
	DE()
	EF()
	FE()
	EA()
	AB()


def AB():
	print("A => B")
	randxy_move(916,297,922,299)
	time.sleep(.2)
	pyautogui.click()
	time.sleep(2+random.random())
	time.sleep(10+ 3*random.random())
def AD():
	print("A => D")
	randxy_move(1615,953,1632,959)
	time.sleep(random.random())
	pyautogui.click()
	time.sleep(4.5+random.random())
def AG():
	print("A => G")
	randxy_move(1745,699,1763,702)
	time.sleep(random.random())
	pyautogui.click()
	time.sleep(6+random.random())
def BA():
	print("B => A")
	randxy_move(1032,873,1046,876)
	time.sleep(random.random())
	pyautogui.click()
	time.sleep(4)
def BC():
	print("B => C")
	randxy_move(792,283,799,289)
	time.sleep(random.random())
	pyautogui.click()
	time.sleep(2.5 + random.random())
	time.sleep(10+ 3*random.random())

def BE():
	print("B => E")
	BA()
	AD()
	DE()

def BF():
	print("B => F")
	BA()
	AD()
	DE()
	EF()

def CB():
	print("C => B")
	randxy_move(1169,860,1180,870)
	time.sleep(random.random())
	pyautogui.click()
	time.sleep(2.5 + random.random())
	time.sleep(10+ 3*random.random())
def DE():
	print("D => E")
	randxy_move(1456,871,1467,879)
	time.sleep(random.random())
	pyautogui.click()
	time.sleep(7+random.random())
def EA():
	print("E => A")
	randxy_move(210,60,213,64)
	time.sleep(random.random())
	pyautogui.click()
	time.sleep(15+random.random())
def EF():
	print("E => F")
	randxy_move(1839,602,1846,606)
	time.sleep(random.random())
	pyautogui.click()
	time.sleep(7+random.random())
def EG():
	print("E => G")
	randxy_move(759,167,765,170)
	time.sleep(random.random())
	pyautogui.click()
	time.sleep(6+random.random())
	time.sleep(10+ 3*random.random())
def FE():
	print("F => E")
	randxy_move(107,485,118,493)
	time.sleep(random.random())
	pyautogui.click()
	time.sleep(7+random.random())
def GA():
	print("G => A")
	randxy_move(276,374,286,380)
	time.sleep(random.random())
	pyautogui.click()
	time.sleep(7+random.random())

def GE():
	print("G => E")
	randxy_move(1163,1000,1178,1003)
	time.sleep(random.random())
	pyautogui.click()
	time.sleep(7+random.random())
	randxy_move(1020,595,1029,604)
	time.sleep(random.random())
	pyautogui.click()
	time.sleep(1 + random.random())


def GI():
	print("G => I")
	randxy_move(1125,335,1136,345)
	time.sleep(random.random())
	pyautogui.click()
	time.sleep(6+random.random())
	time.sleep(10+ 3*random.random())
def IH():
	print("I => H")
	randxy_move(1222,715,1236,722)
	time.sleep(random.random())
	pyautogui.click()
	time.sleep(6+random.random())
	time.sleep(10+ 3*random.random())

def HG():
	print("H => G")
	randxy_move(513,597,525,605)
	time.sleep(random.random())
	pyautogui.click()
	time.sleep(6+random.random())
	time.sleep(10+ 3*random.random())


def F_reset():
	print("F Reset")
	
	pick = random.randint(1,100)
	if pick <= 100:
		#path 1
		randxy_move(1347,135,1355,139)
		time.sleep(random.random())
		pyautogui.click()
		time.sleep(10)
		randxy_move(953,200,970,209)
		time.sleep(random.random())
		pyautogui.click()
		time.sleep(7+random.random())
		randxy_move(1265,200,1275,207)
		time.sleep(random.random())
		pyautogui.click()
		time.sleep(8.5 + random.random())
		randxy_move(67,785,85,795)
		time.sleep(random.random())
		pyautogui.click()
		time.sleep(12 + random.random())
		randxy_move(943,1000,945,1025)
		time.sleep(random.random())
		pyautogui.click()
		time.sleep(5 + random.random())
		pyautogui.click()
		time.sleep(5 + random.random())
		randxy_move(881,872,887,876)
		time.sleep(random.random())
		pyautogui.click()
		time.sleep(4 + random.random())

	else:
		#path2
		bezier3(1007,102)
		x=0
		while(x<3):
			time.sleep(random.random())
			pyautogui.click()
			time.sleep(8)
			x+=1
		bezier3(893,1009)
		x=0
		while(x<4):
			time.sleep(random.random())
			pyautogui.click()
			time.sleep(8)
			x+=1
		time.sleep(2+random.random())
		randxy_move(1022,648,1030,655)
		time.sleep(2+random.random())
		pyautogui.click()

		





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

if __name__ == '__main__':
	main()