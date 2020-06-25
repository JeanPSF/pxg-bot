import cv2

bushGatherPokemons1 = []
# Bottom of Celadon/Saffron rotation
def loadBushGatherPokemons1():
    loadOddish()
    loadBellsprout()
    return bushGatherPokemons1

def loadOddish():
    frontOddish = cv2.imread('./imgs/pokemons/oddish/oddish_front_1.jpg')
    frontOddish_width, frontOddish_height = frontOddish.shape[:-1]
    bushGatherPokemons1.append({
        'name': 'Oddish',
        'buffer': frontOddish,
        'height': frontOddish_height,
        'width': frontOddish_width,
        'threshold': 0.65
    })
    backOddish = cv2.imread('./imgs/pokemons/oddish/oddish_back_1.jpg')
    backOddish_width, backOddish_height = backOddish.shape[:-1]
    bushGatherPokemons1.append({
        'name': 'Oddish',
        'buffer': backOddish,
        'height': backOddish_height,
        'width': backOddish_width,
        'threshold': 0.65
    })
    leftOddish = cv2.imread('./imgs/pokemons/oddish/oddish_left_1.jpg')
    leftOddish_width, leftOddish_height = leftOddish.shape[:-1]
    bushGatherPokemons1.append({
        'name': 'Oddish',
        'buffer': leftOddish,
        'height': leftOddish_height,
        'width': leftOddish_width,
        'threshold': 0.65
    })
    rightOddish = cv2.imread('./imgs/pokemons/oddish/oddish_right_1.jpg')
    rightOddish_width, rightOddish_height = rightOddish.shape[:-1]
    bushGatherPokemons1.append({
        'name': 'Oddish',
        'buffer': rightOddish,
        'height': rightOddish_height,
        'width': rightOddish_width,
        'threshold': 0.65
    })

def loadBellsprout():
    frontBellsprout = cv2.imread('./imgs/pokemons/bellsprout/bellsprout_front_1.jpg')
    frontBellsprout_width, frontBellsprout_height = frontBellsprout.shape[:-1]
    bushGatherPokemons1.append({
        'name': 'Bellsprout',
        'buffer': frontBellsprout,
        'height': frontBellsprout_height,
        'width': frontBellsprout_width,
        'threshold': 0.65
    })
    backBellsprout = cv2.imread('./imgs/pokemons/bellsprout/bellsprout_back_1.jpg')
    backBellsprout_width, backBellsprout_height = backBellsprout.shape[:-1]
    bushGatherPokemons1.append({
        'name': 'Bellsprout',
        'buffer': backBellsprout,
        'height': backBellsprout_height,
        'width': backBellsprout_width,
        'threshold': 0.65
    })
    leftBellsprout = cv2.imread('./imgs/pokemons/bellsprout/bellsprout_left_1.jpg')
    leftBellsprout_width, leftBellsprout_height = leftBellsprout.shape[:-1]
    bushGatherPokemons1.append({
        'name': 'Bellsprout',
        'buffer': leftBellsprout,
        'height': leftBellsprout_height,
        'width': leftBellsprout_width,
        'threshold': 0.65
    })
    rightBellsprout = cv2.imread('./imgs/pokemons/bellsprout/bellsprout_right_1.jpg')
    rightBellsprout_width, rightBellsprout_height = rightBellsprout.shape[:-1]
    bushGatherPokemons1.append({
        'name': 'Bellsprout',
        'buffer': rightBellsprout,
        'height': rightBellsprout_height,
        'width': rightBellsprout_width,
        'threshold': 0.65
    })