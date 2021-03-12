import random
import hashlib
def _create(userParms):
    result = dict.fromkeys(['grid', 'score', 'Integrity', 'status'])
    result['grid'] = '0'
    gridWidth = 4 # predetermined by game ruleset
    gridHeight = 4 # predetermined by game ruleset
    totalGridTiles = gridWidth * gridHeight
    gameGridList = [0] * totalGridTiles
    firstRandomTile = random.randint(0,15)
    secondRandomTile = random.randint(0,15) 
    while (firstRandomTile == secondRandomTile):
        secondRandomTile = random.randint(0,15)
    gameGridList[firstRandomTile] = 2
    gameGridList[secondRandomTile] = 2     
    gameGridString = ''
    for value in gameGridList:
        gameGridString += str(value)
    result['grid'] = gameGridString
    result['score'] = 0
    result['status'] = 'ok'
    # program pulled from Assignment 4 Project Specs
    stringToHash = gameGridString + '.' + str(result['score'])
    integrity = digestHash(stringToHash)
    result['Integrity'] = integrity
    
    return result

def digestHash(stringToHash):
    myHash = hashlib.sha256()
    myHash.update(stringToHash.encode())
    integrityScore = myHash.hexdigest().upper()
    return integrityScore