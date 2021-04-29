'''
Created on Mar 19, 2021

@author: Alex Weeden
'''

import random
import hashlib
import string

def _shift(userParms):
    isErrorFound, error = checkKeys(userParms)
    if isErrorFound:
        return error
       
    result = dict.fromkeys(['grid', 'score', 'integrity', 'status'])

    score = int(userParms['score'])
    result['integrity'] = userParms['integrity'].lower()
    
    if 'direction' not in userParms or userParms['direction'] == '':
        userParms['direction'] = 'down'
    chosenDirection = userParms['direction']
        
    gameGridList, isGridInvalid = parseGrid(userParms['grid'])
    if isGridInvalid:
        return {'status': 'error - invalid grid'}
    
    orientedGrid = flipBoard(gameGridList, chosenDirection)
    combinedGrid, score, isBoardFull = combineTiles(orientedGrid, score)
    if isBoardFull:
        return {'status' : 'error - no shift possible'}
    result['score'] = str(score)
    
    finalGrid = flipBoard(combinedGrid, chosenDirection)
    finalGrid = addTile(finalGrid) 
    
    finalGridString = ''.join(map(str, finalGrid))  
    result['grid'] = finalGridString
    
    status = assessRound(finalGrid)
    result['status'] = status
    
    stringToHash = finalGridString + '.' + result['score']
    integrity = genIntegrity(stringToHash)
    result['integrity'] = integrity
    
    return result

def checkKeys(parms):
    requiredKeys = ['grid','score','integrity']
    acceptedDirections = ['up','down','left','right', '']
    error = {'status': 'ok'}
    for key in requiredKeys:
        if key not in parms:
            error['status'] = ('error - missing ' + key)
            return True, error
    if parms['score'] == '':
        error['status'] = 'error - missing score'
        return True, error
    if len(parms['integrity']) != 64:
        error['status'] = 'error - invalid integrity'
        return True, error
    for character in parms['integrity']:
        if character not in (set(string.hexdigits)):
            error['status'] = 'error - invalid integrity'
            return True, error
    try:
        intScore = int(parms['score'])
    except ValueError:
        error['status'] = 'error - non-int score'
        return True, error
    if intScore % 2 != 0:
        error['status'] = 'error - invalid score'
        return True, error
    if intScore < 0:
        error['status'] = 'error - out of bounds score'
        return True, error
    try:
        direct = parms['direction'].lower()
    except KeyError:
        return False, error
    if direct not in acceptedDirections:
        error['status'] = 'error - invalid direction'
        return True, error
    
        
    return False, error
def combineTiles(grid, score):
    isBoardFull = False
    collapseTiles(grid)
    for i in range(15,3,-1):
        if grid[i] == grid[i-4]:
            grid[i] *= 2
            score += grid[i]
            grid[i-4] = 0
    collapseTiles(grid)
    if 0 not in grid:
        isBoardFull = True
    return grid, score, isBoardFull

def assessRound(grid):
    if 2048 in grid:
        return 'win'
    if 0 not in grid:
        
        return 'lose'
    return 'ok'

def genIntegrity(stringToHash):
    myHash = hashlib.sha256()
    myHash.update(stringToHash.encode())
    integrityScore = myHash.hexdigest().upper()
    return integrityScore

def parseGrid(grid):
    parseIndex = 0
    inputGrid = [0] * 16
    
    for tile in range(16):
        try:
            grid[parseIndex]
        except IndexError:
            return grid, True
        if grid[parseIndex] == '0':
            inputGrid[tile] = 0
            parseIndex += 1
            continue
        else:
            for power in range(1,11): # Only need to check to 2^10 = 1024
                value =  pow(2, power)
                strValue = str(value)
                if grid[parseIndex:parseIndex+len(strValue)] == strValue:
                    inputGrid[tile] = value
                    parseIndex += len(strValue)
                    break    
    try:
        grid[parseIndex]
    except IndexError:
        return inputGrid, False
    return inputGrid, True


def flipBoard(gameGrid, direction):
    finalGrid = [0]*16
    if direction == 'up':
        finalGrid = flipVertical(gameGrid)
    elif direction == 'down':
        finalGrid = gameGrid
    elif direction == 'left':
        finalGrid = flipLeft(gameGrid)
    elif direction == 'right':
        finalGrid = flipRight(gameGrid)
    else:
        finalGrid = gameGrid
    return finalGrid

def flipVertical(gameGrid):
    flippedGrid = [0] * 16
    for i in range(16):
        flippedGrid[i] = gameGrid[15-i]
    return flippedGrid

def flipRight(gameGrid):
    flippedGrid = [0] * 16    
    x = 0 # for x in range
    for i in range(4):
        for j in range(0,13,4):
            flippedGrid[x] = gameGrid[i+j]
            x += 1
    return flippedGrid

def flipLeft(gameGrid):
    flippedGrid = [0] * 16
    x = 0
    for i in range(4):
        for j in range(0,13,4):
            flippedGrid[x] = gameGrid[15-(i+j)]
            x += 1
    return flippedGrid


def collapseTiles(gameGrid):  
    isDone = False
    while(not isDone):
        isDone = True
        for i in range(15,3,-1):
            tileAbove = i-4
            if gameGrid[i] == 0 and gameGrid[tileAbove] != 0:
                gameGrid[i] = gameGrid[tileAbove]
                gameGrid[tileAbove] = 0
                isDone = False
    return gameGrid

def addTile(gameGrid):
    indexOfTile = 0
    emptyTiles = []
    for tile in gameGrid:
        if tile == 0:
            emptyTiles.append(indexOfTile)
        indexOfTile += 1
    newTileIndexChoice = random.choice(emptyTiles)
    newTileValue = random.choice([2,4])
    gameGrid[newTileIndexChoice] = newTileValue
    return gameGrid
        