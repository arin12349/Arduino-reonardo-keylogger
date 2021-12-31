from pynput.keyboard import Key, Listener
import serial
from time import sleep
from random import *
import logger

ser = serial.Serial(port='COM3',
    baudrate=9600)


alt = '1'
shift = '2'
up = '3'
down = '4'
left = '5'
right = '6'

aalt = alt.encode('utf-8')
ashift = shift.encode('utf-8')
adown = down.encode('utf-8')
aleft = left.encode('utf-8')
aright = right.encode('utf-8')
aup = up.encode('utf-8')

na = []
mil = 0
mil2 = 0
state = 0

def readfile():
    global na
    mil = 0
    mil2 = 0
    ma = []
    f = open('KeyLog.txt', 'r')
    while True:
        a = f.readline()
        if a == '':
            f.close()
            break

        mil2 = int(int(a[14:16])*60000) + int(a[17:19] + a[20:23])
        #mil2 = a[17:19] + a[20:23]
        if mil != 0:
            ma.append(int(mil2) - int(mil))
        ma.append(a[25:-1])
        
        mil = int(int(a[14:16])*60000) + int(a[17:19] + a[20:23])

    na.append(ma)
    f.close()

def readfile2():
    global na
    mil = 0
    mil2 = 0
    ma = []
    f = open('KeyLog2.txt', 'r')
    while True:
        a = f.readline()
        if a == '':
            f.close()
            break

        mil2 = int(int(a[14:16])*60000) + int(a[17:19] + a[20:23])
        #mil2 = a[17:19] + a[20:23]
        if mil != 0:
            ma.append(int(mil2) - int(mil))
        ma.append(a[25:-1])
        
        mil = int(int(a[14:16])*60000) + int(a[17:19] + a[20:23])

    na.append(ma)
    f.close()


def readfile3():
    global na
    mil = 0
    mil2 = 0
    ma = []
    f = open('KeyLog3.txt', 'r')
    while True:
        a = f.readline()
        if a == '':
            f.close()
            break

        mil2 = int(int(a[14:16])*60000) + int(a[17:19] + a[20:23])
        #mil2 = a[17:19] + a[20:23]
        if mil != 0:
            ma.append(int(mil2) - int(mil))
        ma.append(a[25:-1])
        
        mil = int(int(a[14:16])*60000) + int(a[17:19] + a[20:23])

    na.append(ma)
    f.close()

    
def press(key):
    global state
    if key == Key.f1:
        #start record
        state = 1
        return False

    if key == Key.f8:
        state = 2
        return False

    else:
        print(key)

def press_loop(key):
    if key == Key.f2:
        return False
    else:
        print(key)

def loop():
    global na
    ma = []
    readfile()
    readfile2()
    readfile3()
    print("start looping")
    with Listener(on_press=press_loop) as listener2:
        while True:
            num = randint(0,2)
            print(num)
            ma = na[num]
            if not listener2.running:
                print("stop looping")
                break
            for i in range(len(ma)):
                if (i % 2 != 1):
                    print(ma[i])
                    if ma[i] == "Key.alt_l":
                        tmp = aalt
                    elif ma[i] == "Key.shift":
                        tmp = ashift
                    elif ma[i] == "Key.up":
                        tmp = aup
                    elif ma[i] == "Key.down":
                        tmp = adown
                    elif ma[i] == "Key.left":
                        tmp = aleft
                    elif ma[i] == "Key.right":
                        tmp = aright
                    else:
                        tmp = ma[i].encode('utf-8')

                    ser.write(tmp)
                        
                else:
                    print(ma[i] / 1000)
                    sleep(uniform(0.05, 0.15) + ma[i] / 1000)
                    
            sleep(2)
                    

print("aa")
while True:
    with Listener(on_press=press) as listener1:
        listener1.join()
    if state == 1:
        #record
        logger.start()
    elif state == 2:
        #looping
        loop()
