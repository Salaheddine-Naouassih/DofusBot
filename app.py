import cv2
import pyautogui
import time
import random
import keyboard
import pyperclip
from PIL import Image

import requests
import scapy.all as scapy

import pytesseract
from gethints import * 

global direction, element

pos = [[1125, 1053], [92, 16], [701, 322], [1042, 325]]

#AJUSTER Dofus_X et Dofus_Y pour ouvrir DOFUS depuis la barre de taches
def Open_Dofus():
    Dofus_X = 1184
    Dofus_Y = 1051
    pyautogui.moveTo(Dofus_X, Dofus_Y)
    pyautogui.click()
    time.sleep(0.25)

#AJUSTER Chrome_X et Chrome_Y pour ouvrir CHROME depuis la barre de taches
def Open_Chrome():
    Chrome_X = 1125
    Chrome_Y = 1053
    pyautogui.moveTo(Chrome_X, Chrome_Y)
    pyautogui.click()
    time.sleep(0.25)

#AJUSTER X et Y pour match position de l'onglet dofusdb chasse au tresor
def Open_Chasse():
    X=92
    Y=16
    pyautogui.moveTo(X, Y)
    time.sleep(0.25)
    pyautogui.click()

#AJUSTER les coordonees de region pour screen la pos en haut a gauche de l'ecran 
def ScreenShot_Starting_Pos():
    pyautogui.screenshot('starting_pos.png', region=(111, 196, 51, 16))
    time.sleep(0.25)


#extrait la la position de votre charactere en jeu depuis le screenshot 
def Parse_Pos(text):
    # parse position with delimiter , and convert to int X and Y
    pos = pytesseract.image_to_string(Image.open(text))
    print('posizione: ', pos)
    #create a loop to keep taking screenshots 
    # delimit from , to get X and Y
    posX = pos.split(",", 1)[0]
    posY = pos.split(",", 1)[1]
    # remove [ and ] from the string
    posX = posX.replace('[', '')
    posY = posY.replace(']', '')
    print('pos X: ', posX)
    print('pos Y: ', posY)
    return posX, posY


#on colle les pos sur les inputs de dofusdb chasse au tresor
def Paste_Pos(posX, posY):
    # move cursor to pos X
    pyautogui.moveTo(701, 322)#ici
    time.sleep(0.25)
    pyautogui.click()
    #clear input
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('delete')
    # paste posX in the input
    pyautogui.write(str(posX))
    time.sleep(0.1)
    # move cursor to pos Y
    pyautogui.moveTo(1042, 325)#ici
    time.sleep(0.25)
    pyautogui.click()
    #clear input
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('delete')
    # paste posY in the input
    pyautogui.write(str(posY))
    time.sleep(0.1)

    # move to deadpoint


#j'ai oublier pk mais ca avait une utilite
def Move_To_DeadPoint():
    pyautogui.moveTo(539, 16)
    time.sleep(0.25)
    pyautogui.click()

#on bouge la souris pour hover sur l'UI de chasse au tresor en jeu pour screenshot le text, ajuster les coordonnees de region 
def Get_Hint(i):
    # get hint
    pyautogui.moveTo(79, 230+30*i)
    hint_name = 'hint'+str(i)+'.png'
    pyautogui.screenshot(hint_name, region=(27, 153+30*i, 360, 60))
    time.sleep(0.20)


#ca parse les indices depuis le screenshot 
def Parse_Hint(i):
    # parse hint
    hint_name = 'hint'+str(i)+'.png'
    # parse hint with psm option 6 

    hint = pytesseract.image_to_string(Image.open(hint_name), config='--psm 6')
    #strip hint from {, }, [, ], (, ), <, >, /, \, |, ~, `, !, @, #, $, %, ^, &, *, -, _, +, =, :, ;, ", ', ?, ., ,, 
    #do it in a loop 
    for char in hint:
        if char in ['{', '}','(', ')', '<', '>', '/', '\\', '|', '~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '-', '_', '+', '=', ':', ';', '"', '?', '.', ',']:
            hint = hint.replace(char, '')
 
    print('hint: ', hint)
    # parse hint for nord/est/ouest/sud
    if 'nord' in hint:
        direction = 'nord'
    elif 'est' in hint:
        direction = 'est'
    elif 'ouest' in hint:
        direction = 'ouest'
    elif 'sud' in hint:
        direction = 'sud'
    # parse elment 'jusqu'a [element]'
    element = ''
    #black magic
    temp= hint.split('[')
    hint1=temp[1].split(']')
    #get rid of \n and \r
    temp=hint1[0].replace('\n',' ')
    temp=temp.replace('  ',' ')


    element = temp
    return element, direction


Positions = []

def move_to_chasse_deadpoint():
    pyautogui.moveTo(220, 1006)
    time.sleep(0.25)
    pyautogui.click()

#vaut mieux utiliser les fonctions dans gethints.py
def Look_For_Hint(posX, posY, direction, element):
    Open_Chrome()
    Open_Chasse()
    Paste_Pos(posX, posY)
    move_to_chasse_deadpoint()
    time.sleep(0.25)
    if direction == 'nord':
        print('GOIING NORTH')
        # click north
        pyautogui.moveTo(954, 483)
        pyautogui.click()
        time.sleep(1)
    elif direction == 'est':
        print('GOIING EAST')
        # click east
        pyautogui.moveTo(1018, 503)
        pyautogui.click()
        time.sleep(1)
    elif direction == 'ouest':
        print('GOIING WEST')
        # click west
        pyautogui.moveTo(898, 517)
        pyautogui.click()
        time.sleep(1)
    elif direction == 'sud':
        print('GOIING SOUTH')
        # click south
        pyautogui.moveTo(949, 561)
        pyautogui.click()
        time.sleep(1)

    # click input
    pyautogui.moveTo(1055, 675)
    pyautogui.click()
    Elem= str(element)
    pyperclip.copy(Elem)
    pyautogui.hotkey('ctrl', 'v')
    #copy Elem into paper clip 
    pyperclip.copy(Elem)
    checkelem=pyperclip.paste()
    print('checkelem:',checkelem)
    time.sleep(3)
    # chose option
    pyautogui.moveTo(1055, 716)
    pyautogui.click()

    Open_Dofus()
    pyautogui.moveTo(186, 1009)
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    pyautogui.press('enter')
    time.sleep(1)


def get_pos():
    coor1 = pyperclip.paste()
    coor1.split(" ")
    coox1 = coor1.split(" ")[1]
    cooy1 = coor1.split(" ")[2]
    print(coox1)
    print(cooy1)
    return coox1, cooy1

def get_starting_pos():
    pyautogui.screenshot('starting_pos.png', region=(107, 193, 55, 19))
    time.sleep(0.25)
    temp=Parse_Pos('starting_pos.png')
    return temp

def get_current_pos():
    pyautogui.screenshot('current_pos.png', region=(16, 76, 78, 28))
    time.sleep(0.65)
    temp= Parse_current_pos()    
    return temp

def Parse_current_pos():
    # parse posizione with delimiter , and convert to int X and Y
    temp=pytesseract.image_to_string(Image.open('current_pos.png'))
    # delimit from , to get X and Y
    posX = temp.split(",", 1)[0]
    posY = temp.split(",", 1)[1]
    # remove , from the string
    posX = posX.replace(',', '')
    posY = posY.replace(',', '')
    print('posizione X: ', posX)
    print('posizione Y: ', posY)
    return posX, posY



def is_not_matching(current_posX, current_posY, posX, posY):
    #str to int for comparison
    current_posX = int(current_posX)
    current_posY = int(current_posY)
    posX = int(posX)
    posY = int(posY)
    if (current_posX == posX and current_posY == posY):
        print('TADAAAA')
        return False
    else:
     
        return True

Open_Dofus()
for i in range(0, 5):
    
    if i == 0:
        pos = ScreenShot_Starting_Pos()
        posX, posY = Parse_Pos('starting_pos.png')

    Move_To_DeadPoint()
    Get_Hint(i)
    element, direction = Parse_Hint(i)
    print('element: ', element)
    print('direction: ', direction)
    #check element for subtring phorreur
    if 'Phorreur' in element:
            print('moving to phorreur')
            if keyboard.read_key() == "y":
                i+=1
                continue
    Look_For_Hint(posX, posY, direction, element)
    posX, posY = get_pos()

    current_pos = get_current_pos()
    destination=get_pos()

    print('current_pos: ', current_pos)
    print('destination: ', destination)

    while (is_not_matching(current_pos[0], current_pos[1], destination[0], destination[1])):
        print('not matching')
        current_pos = get_current_pos()
        coors=get_pos()
        time.sleep(1)
    pyautogui.moveTo(301, 230+30*i)
    pyautogui.click()
    i += 1
    time.sleep(1)

