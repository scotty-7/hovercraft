from evdev import InputDevice, categorize, ecodes
import RPi.GPIO as GPIO

print("Button mapping test")

#creates object 'gamepad' to store the data
gamepad = InputDevice('/dev/input/event3')

#Create a class to store gamepad vaiables
class pad:
	a = 0
	b = 0
	x = 0
	y = 0
	sl = 0
	sr = 0
	p = 0
	m = 0
	bl = 0
	br = 0
	tl = 0
	tr = 0
	s = 0
	c = 0
	l_y = 0
	l_x = 0
	r_y = 0
	r_x = 0

#button codes
aBtn = 305
bBtn = 304
yBtn = 306
xBtn = 307 
bl = 308
br = 309
tl = 310
tr = 311
m = 312
p = 313
sl = 314
sr = 315
c = 316
s = 317

pro = pad()

#loop and filter by event code and print the mapped label
for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        if event.value == 1:
            if event.code == aBtn:
            	pro.a = 1
            elif event.code == bBtn:
                pro.b = 1
            elif event.code == xBtn:
                pro.x = 1
            elif event.code == yBtn:
                pro.y = 1
            elif event.code == bl:
                pro.bl = 1
            elif event.code == br:
                pro.br = 1
            elif event.code == tl:
                pro.tl = 1
            elif event.code == tr:
                pro.tr = 1
            elif event.code == m:
                pro.m = 1
            elif event.code == p:
                pro.p = 1
            elif event.code == sl:
                pro.sl = 1
            elif event.code == sr:
                pro.sr = 1
            elif event.code == c:
                pro.c = 1
            elif event.code == s:
                pro.s = 1
        elif event.value == 0:
            if event.code == aBtn:
            	pro.a = 0
            elif event.code == bBtn:
                pro.b = 0
            elif event.code == xBtn:
                pro.x = 0
            elif event.code == yBtn:
                pro.y = 0
            elif event.code == bl:
                pro.bl = 0
            elif event.code == br:
                pro.br = 0
            elif event.code == tl:
                pro.tl = 0
            elif event.code == tr:
                pro.tr = 0
            elif event.code == m:
                pro.m = 0
            elif event.code == p:
                pro.p = 0
            elif event.code == sl:
                pro.sl = 0
            elif event.code == sr:
                pro.sr = 0
            elif event.code == c:
                pro.c = 0
            elif event.code == s:
                pro.s = 0
    elif event.type == ecodes.EV_ABS:
    	#print(event)
        if(event.code == 0):
        	pro.l_x = event.value - 32215
        if(event.code == 1): #axis 1 is the vertical axis on the left stick
        	pro.l_y = -event.value + 34452
    print pro.l_x, pro.l_y;