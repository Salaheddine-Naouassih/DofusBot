
import cv2
import pyautogui 
import time
import random
import keyboard




print('Press Ctrl-C to quit.')
array = []
i = 0
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
        if keyboard.is_pressed('q'):
            print('pos['+str(i)+'] = ['+str(x)+','+str(y)+'] saved')
            array.append([i,x,y])
            i = i + 1
            time.sleep(0.1)

except KeyboardInterrupt:
    print(array)
    print('\n')