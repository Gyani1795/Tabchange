import time,pyautogui
import random
#import subprocess


pyautogui.PAUSE = 1
pyautogui.FAILSAFE = False
#naresh143@rupayamail.com
#Gyanilal1

#x,y = pyautogui.position()
#a=['chromium','firefox','sublime']
#for i in a:
#	subprocess.run(i)
try:
	while True:
		x,y = pyautogui.size()
		x = random.randint(300,x)
		y = random.randint(200,y)
		#print(x,y)
		pyautogui.moveTo(x,y)
		pyautogui.hotkey("Alt","Shift","Tab")
		pyautogui.scroll(10)
		time.sleep(2)
except KeyboardInterrupt:
	print("\nDone")
