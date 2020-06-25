from env import env 
import cv2

screen_center_x = int(1920/2 - 64 - 48)
screen_center_y = int(1080/2 - 48)

def getCharacter(img):
    if env['debug']:
        cv2.rectangle(
            img, (screen_center_x - 32, screen_center_y - 32), (screen_center_x - 32 + 64, screen_center_y - 32 + 64), (0, 0, 255), 2)
    return {'position': {
                    'x': screen_center_x,
                    'y': screen_center_y
                }
            }
