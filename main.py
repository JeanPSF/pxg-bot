### System Modules ###
import sys
sys.path.append(
    "./modules")
sys.path.append(
    "./modules/computerVision/bushs")
sys.path.append(
    "./modules/computerVision/pokemons")
import time
import keyboard
import pyautogui
from env import env, path
### Load Bot Modules ###
from professorGather import gather
from system import getFrame
from character import getCharacter
from autoPath import autoPath, autoPathWithMouse
### Image Process Modules ###
import cv2
### Computer Vision Modules ###
from bushsTier1 import loadBushsTier1
from bushGatherPokemons import loadBushGatherPokemons1

### Screen Config ###
screenConfig = {
    'screen_center_x': int(1920/2 - 64 - 48),
    'screen_center_y': int(1080/2 - 48)
}
### Actions Config ###
botConfig = {
    'status': 'active'
}
professorGatherConfig = {
    'status': True,
    'bushTier': 1
}
walkConfig = {
    'status': True,
    'path': path,
    'step': 0
}
### Computer Vision Config ###
computerVision = {
    'bushsTier1': loadBushsTier1(),
}
if professorGatherConfig['status'] == True:
    computerVision['bushsTier1'] = loadBushsTier1()
if walkConfig['status'] == True:
    computerVision['pokemons'] = loadBushGatherPokemons1()

while True:
    if botConfig['status'] != 'paused':
        frame = getFrame()
        ### Load Computer Vision ###
        character = getCharacter(frame)
        ### Load Bot Actions ###
        if professorGatherConfig['status']:
            gather(professorGatherConfig, character, frame, computerVision)
        if walkConfig['status']:
            #autoPath(walkConfig)
            autoPathWithMouse(walkConfig, character, frame, computerVision)
        if env['debug'] == True:
            cv2.imshow("Screen", frame)
        if keyboard.is_pressed('p'):
            botConfig['status'] = 'paused'
    else:
        if keyboard.is_pressed('a'):
            botConfig['status'] = 'active'
        print('Bot paused!')
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
