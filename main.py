### System Modules ###
import sys
sys.path.append(
    "./modules")
sys.path.append(
    "./modules/computerVision/bushs")
import time
### Load Bot Modules ###
from professorGather import gather
from system import getFrame
from character import getCharacter
### Image Process Modules ###
import cv2
### Computer Vision Modules ###
from bushsTier1 import loadBushsTier1

### Screen Config ###
screenConfig = {
    'screen_center_x': int(1920/2 - 64 - 48),
    'screen_center_y': int(1080/2 - 48)
}
### Actions Config ###
professorGatherConfig = {
    'status': True,
    'bushTier': 1
}
walk = {
    'status': False,
    'path': []
}
### Computer Vision Config ###
computerVision = {
    'bushsTier1': loadBushsTier1()
}

while True:
    frame = getFrame()
    ### Load Computer Vision ###
    character = getCharacter(frame)
    ### Load Bot Actions ###
    if professorGatherConfig['status']:
        gather(professorGatherConfig, character, frame, computerVision)
    # time.sleep(0.05)
    cv2.imshow("Screen", frame)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
