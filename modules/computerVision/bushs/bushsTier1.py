import cv2
### Load Bush's ###
bushsTier1 = []
def loadBushsTier1():
    bush1 = cv2.imread('./imgs/bushsTier1/bush1.jpg')
    bush1_width, bush1_height = bush1.shape[:-1]
    bushsTier1.append({
        'name': 'simple',
        'buffer': bush1,
        'height': bush1_height,
        'width': bush1_width,
        'threshold': 0.65
    })
    bush2 = cv2.imread('./imgs/bushsTier1/bush2.jpg')
    bush2_width, bush2_height = bush2.shape[:-1]
    bushsTier1.append({
        'name': 'double',
        'buffer': bush2,
        'height': bush2_height,
        'width': bush2_width,
        'threshold': 0.65
    })
    bush3 = cv2.imread('./imgs/bushsTier1/bush3.jpg')
    bush3_width, bush3_height = bush3.shape[:-1]
    bushsTier1.append({
        'name': 'triple',
        'buffer': bush3,
        'height': bush3_height,
        'width': bush3_width,
        'threshold': 0.62
    })
    bigbush = cv2.imread('./imgs/bushsTier1/bigbush.jpg')
    bigbush_width, bigbush_height = bigbush.shape[:-1]
    bushsTier1.append({
        'name': 'giant',
        'buffer': bigbush,
        'height': bigbush_height,
        'width': bigbush_width,
        'threshold': 0.65
    })
    return bushsTier1