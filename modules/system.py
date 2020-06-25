import cv2
import numpy as np
from PIL import ImageGrab
from env import env

### Get a game frame ###
def getFrame(): 
    return cv2.cvtColor(np.array(ImageGrab.grab()), cv2.COLOR_BGR2RGB)

### Compare the distance between two objects ###
def isNear(obj1, obj2, diagonal = False, frame = None):  # obj1 => bush - obj2 => player
    if frame != None and env['debug'] == True:
        cv2.rectangle(
            frame, (int(obj1[0]-1), int(obj1[1]-1)), (int(obj1[0]+1), int(obj1[1]+1)), (0, 255, 0), 2)
        cv2.rectangle(
            frame, (int(obj2[0]-1), int(obj2[1]-1)), (int(obj2[0]+1), int(obj2[1]+1)), (0, 255, 0), 2)
    if not diagonal:
        # horizontal
        if obj1[0] > obj2[0] and obj1[0] - obj2[0] < 93 and (obj1[1] - obj2[1] < 40 and obj1[1] - obj2[1] > - 40):
            # bush a esquerda
            return 'west'
        elif obj1[0] < obj2[0] and obj2[0] - obj1[0] < 93 and (obj1[1] - obj2[1] < 40 and obj1[1] - obj2[1] > - 40):
            # bush a direita
            return 'east'
        # vertical
        elif obj1[1] > obj2[1] and obj1[1] - obj2[1] < 93 and (obj1[0] - obj2[0] < 40 and obj1[0] - obj2[0] > - 40):
            # bush acima
            return 'north'
        elif obj1[1] < obj2[1] and obj2[1] - obj1[1] < 93 and (obj1[0] - obj2[0] < 40 and obj1[0] - obj2[0] > - 40):
            # bush abaixo
            return 'south'
        else:
            return 'far'
    elif diagonal:
        # horizontal
        if obj1[0] > obj2[0] and obj1[0] - obj2[0] < 93 and (obj1[1] - obj2[1] < 40 and obj1[1] - obj2[1] > - 40):
            # bush a esquerda
            return 'west'
        elif obj1[0] < obj2[0] and obj2[0] - obj1[0] < 93 and (obj1[1] - obj2[1] < 40 and obj1[1] - obj2[1] > - 40):
            # bush a direita
            return 'east'
        # vertical
        elif obj1[1] > obj2[1] and obj1[1] - obj2[1] < 93 and (obj1[0] - obj2[0] < 40 and obj1[0] - obj2[0] > - 40):
            # bush acima
            return 'north'
        elif obj1[1] < obj2[1] and obj2[1] - obj1[1] < 93 and (obj1[0] - obj2[0] < 40 and obj1[0] - obj2[0] > - 40):
            # bush abaixo
            return 'south'
        # diagonais

        else:
            return 'far'

### Compare the distance between two objects ###
def isFar(obj1, obj2, direction = 'any', frame = None):  # obj1 => bush - obj2 => player
    if frame != None and env['debug'] == True:
        cv2.rectangle(
            frame, (int(obj1[0]-1), int(obj1[1]-1)), (int(obj1[0]+1), int(obj1[1]+1)), (0, 255, 0), 2)
        cv2.rectangle(
            frame, (int(obj2[0]-1), int(obj2[1]-1)), (int(obj2[0]+1), int(obj2[1]+1)), (0, 255, 0), 2)
    if direction == 'num6':
        if obj1[0] < obj2[0] and obj2[0] - obj1[0] < 93 and (obj1[1] - obj2[1] < 40 and obj1[1] - obj2[1] > - 40):
            # pkmn a direita
            return False
        else: return True
    elif direction == 'num4':
        if obj1[0] > obj2[0] and obj1[0] - obj2[0] < 93 and (obj1[1] - obj2[1] < 40 and obj1[1] - obj2[1] > - 40):
            # pkmn a esquerda
            return False
        else: return True
    elif direction == 'num8':
        if obj1[1] > obj2[1] and obj1[1] - obj2[1] < 93 and (obj1[0] - obj2[0] < 40 and obj1[0] - obj2[0] > - 40):
            # pkmn acima
            return False
        else: return True
    elif direction == 'num2':
        if obj1[1] < obj2[1] and obj2[1] - obj1[1] < 93 and (obj1[0] - obj2[0] < 40 and obj1[0] - obj2[0] > - 40):
            # pkmn abaixo
            return False
        else: return True
    else : return True

