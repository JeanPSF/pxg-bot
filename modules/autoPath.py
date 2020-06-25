import pyautogui
import time
import cv2
import numpy as np
from system import isNear, isFar
from env import env, path

def movementAllowed(walkConfig, character, frame, computerVision):
    for pokemon in computerVision['pokemons']:
        pokemonMatches = cv2.matchTemplate(
            frame, pokemon['buffer'], cv2.TM_CCOEFF_NORMED)
        pokemonMatchesLocation = np.where(pokemonMatches >= pokemon['threshold'])
        for match in zip(*pokemonMatchesLocation[::-1]):
            if env['debug'] == True:
                cv2.rectangle(
                    frame, match, (match[0] + pokemon['width'], match[1] + pokemon['height']), (0, 0, 255), 2)
            pokemonPosition = isFar(
                [match[0] + pokemon['width']/2, match[1] + pokemon['height']/2], [character['position']['x'], character['position']['y']], walkConfig['path'][walkConfig['step']])
            if pokemonPosition != 'far':
                if env['debug']:
                    cv2.rectangle(
                        frame, (int(match[0] + pokemon['width']/2 + 5), int(match[1] + pokemon['height']/2 + 5)), (int(match[0] + pokemon['width']/2 - 5), int(match[1] + pokemon['height']/2 - 5)), (255, 0, 0), 2)
                return False
    return True


def autoPathWithMouse(walkConfig, character, frame, computerVision):
    if movementAllowed(walkConfig, character, frame, computerVision) == True:
        if walkConfig['path'][walkConfig['step']] == 'num1':
            pyautogui.moveTo(character['position']['x'] - 64, character['position']['y'] + 64)
            pyautogui.click()
            time.sleep(1)
        elif walkConfig['path'][walkConfig['step']] == 'num2':
            pyautogui.moveTo(character['position']['x'], character['position']['y'] + 64)
            pyautogui.click()
            time.sleep(0.6)
        elif walkConfig['path'][walkConfig['step']] == 'num3':
            pyautogui.moveTo(character['position']['x'] + 64, character['position']['y'] + 64)
            pyautogui.click()
            time.sleep(1)
        elif walkConfig['path'][walkConfig['step']] == 'num4':
            pyautogui.moveTo(character['position']['x'] - 64, character['position']['y'])
            pyautogui.click()
            time.sleep(0.6)
        elif walkConfig['path'][walkConfig['step']] == 'num6':
            pyautogui.moveTo(character['position']['x'] + 64, character['position']['y'])
            pyautogui.click()
            time.sleep(0.6)
        elif walkConfig['path'][walkConfig['step']] == 'num7':
            pyautogui.moveTo(character['position']['x'] - 64, character['position']['y'] - 64)
            pyautogui.click()
            time.sleep(1)
        elif walkConfig['path'][walkConfig['step']] == 'num8':
            pyautogui.moveTo(character['position']['x'], character['position']['y'] - 64)
            pyautogui.click()
            time.sleep(0.6)
        elif walkConfig['path'][walkConfig['step']] == 'num9':
            pyautogui.moveTo(character['position']['x'] + 64, character['position']['y'] - 64)
            pyautogui.click()
            time.sleep(1)
        else:
            print('comando de movimentação inválido.')

        if walkConfig['step'] == len(walkConfig['path']):
            walkConfig['step'] = 0
        else:
            walkConfig['step'] = walkConfig['step'] + 1

def autoPath(walkConfig):
    if walkConfig['path'][walkConfig['step']] == 'up' or walkConfig['path'][walkConfig['step']] == 'down' or walkConfig['path'][walkConfig['step']] == 'left' or walkConfig['path'][walkConfig['step']] == 'right':
        print(str(walkConfig['path'][walkConfig['step']]))
        pyautogui.hotkey('ctrlright', str(walkConfig['path'][walkConfig['step']]))
    else:
        if walkConfig['path'][walkConfig['step']] == 'num1': 
            pyautogui.hotkey('left', 'down')
        elif walkConfig['path'][walkConfig['step']] == 'num3': 
            pyautogui.hotkey('right', 'down')
        elif walkConfig['path'][walkConfig['step']] == 'num7': 
            pyautogui.hotkey('left', 'top')
        elif walkConfig['path'][walkConfig['step']] == 'num9': 
            pyautogui.hotkey('right', 'top')
    if walkConfig['step'] == len(walkConfig['path']):
        walkConfig['step'] = 0
    else:
        walkConfig['step'] = walkConfig['step'] + 1