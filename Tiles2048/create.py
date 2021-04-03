'''
Created on Mar 12, 2021
Creates a starting grid for the game 2048
Returns a dictionary representation of that grid
@author: Alex Weeden
'''
import random
import hashlib
def _create(userParms):
    result = dict.fromkeys(['grid', 'score', 'integrity', 'status'])
    
    result['score'] = '0'
    result['status'] = 'ok'
    
    gameGrid = establishBoard()
    gameGridString = ''
    gameGridString = gameGridString.join(map(str, gameGrid))
    
    result['grid'] = gameGridString
    
    stringToHash = gameGridString + '.' + str(result['score'])
    integrity = genIntegrity(stringToHash)
    result['integrity'] = integrity
    
    return result

# code pulled from Assignment 4 Project Specs
def establishBoard():
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
    
    return gameGridList

def genIntegrity(stringToHash):
    myHash = hashlib.sha256()
    myHash.update(stringToHash.encode())
    integrityScore = myHash.hexdigest().upper()
    return integrityScore
