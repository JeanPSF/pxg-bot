import cv2
import numpy as np
from env import env
from system import isNear
### Bot Modules ###
import pywinauto.keyboard as keyboard
import pywinauto.mouse as mouse

def gatherAction(coordinates):
    pass


def checkBushsTier1(character, frame, bushsList):
    print(bushsList)
    if type(bushsList) == list:
        for bush in bushsList:
            bushMatches = cv2.matchTemplate(
                frame, bush['buffer'], cv2.TM_CCOEFF_NORMED)
            bushMatchesLocation = np.where(bushMatches >= bush['threshold'])
            # Switch collumns and rows
            for match in zip(*bushMatchesLocation[::-1]):
                if env['debug'] == True:
                    cv2.rectangle(
                        frame, match, (match[0] + bush['width'], match[1] + bush['height']), (0, 0, 255), 2)
                bushPosition = isNear(
                    [match[0] + bush['width']/2, match[1] + bush['height']/2], [character['position']['x'], character['position']['y']])
                if bushPosition != 'far':
                    if env['debug']:
                        cv2.rectangle(
                            frame, (int(match[0] + bush['width']/2 + 5), int(match[1] + bush['height']/2 + 5)), (int(match[0] + bush['width']/2 - 5), int(match[1] + bush['height']/2 - 5)), (255, 0, 0), 2)
                    return (int(match[0] + bush['width']/2 + 5), int(match[1] + bush['height']/2 + 5))
    else:
        print('Load bushs tier 1 module please.')


def checkBushsTier2(frame):
    pass


def gather(gatherConfig, character, frame, computerVision):
    if gatherConfig['bushTier'] == 1:
        # gather normal bushs
        result = checkBushsTier1(
            character, frame, computerVision['bushsTier1'])
        if result != None and type(result) == tuple:
            gatherAction(result, frame)
    elif bushTier == 2:
        # gather rank A bushs
        pass
