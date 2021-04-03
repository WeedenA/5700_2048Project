'''
Created on Mar 19, 2021

@author: Alex Weeden
'''

import random
import hashlib

def _shift(userParms):
    isCaught, error = errorCheck(userParms)
    if isCaught:
        return error
    result = dict.fromkeys(['grid', 'score', 'integrity', 'status'])
    
    score = int(userParms['score'])
    result['integrity'] = userParms['integrity']
    
    if 'direction' not in userParms:
        userParms['direction'] = 'down'
    chosenDirection = userParms['direction']
        
    gameGridList, isErrorFound = handleInputGrid(userParms['grid'])
    if isErrorFound:
        return {'status': 'error - invalid grid'}
    
    orientedGrid = flipDirection(gameGridList, chosenDirection, False)
    combinedGrid, score = combine(orientedGrid, score)
    finalGrid = flipDirection(combinedGrid, chosenDirection, True)
    finalGrid = addTile(finalGrid) 
    
    finalGridString = ''.join(map(str, finalGrid))  
    result['grid'] = finalGridString
    
    status = assessRound(result, finalGrid)
    result['status'] = status
    
    result['score'] = str(score)
    
    stringToHash = finalGridString + '.' + result['score']
    integrity = digestHash(stringToHash)
    result['integrity'] = integrity
    
    return result

def errorCheck(parms):
    requiredKeys = ['grid','score','integrity']
    acceptedDirections = ['up','down','left','right']
    error = {'status': 'ok'}
    for key in requiredKeys:
        if key not in parms:
            error['status'] = 'error - missing keys'
            return True, error
    if '0' not in parms['grid']:
        error['status'] = 'error - no shift possible'
        return True, error
    if len(parms['integrity']) != 64:
        error['status'] = 'error - invalid integrity'
        return True, error
    if int(parms['score']) % 2 != 0:
        error['status'] = 'error - invalid score'
        return True, error
    try:
        direct = parms['direction']
    except KeyError:
        return False, error
    if direct not in acceptedDirections:
        error['status'] = 'error - invalid direction'
        return True, error
        
    return False, error
def combine(grid, score):
    collapse(grid)
    grid, score = merge(grid,score)
    collapse(grid)
    return grid, score

def assessRound(parms, grid):
    if 2048 in grid:
        return 'win'
    if 0 not in grid:
        return 'lose'
    return 'ok'

def digestHash(stringToHash):
    myHash = hashlib.sha256()
    myHash.update(stringToHash.encode())
    integrityScore = myHash.hexdigest().upper()
    return integrityScore

def handleInputGrid(grid):
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
                    continue

def flipDirection(gameGrid, direction, isReverse):
    allowedDirections = ['up','down','left','right']
    finalGrid = [0]*16
    if direction == allowedDirections[0]:
        finalGrid = flipUpDown(gameGrid)
    elif direction == allowedDirections[1]:
        finalGrid = gameGrid
    elif direction == allowedDirections[2]:
        if isReverse:
            finalGrid = flipLeftRight(gameGrid)
            finalGrid = flipUpDown(finalGrid)
        else:
            finalGrid = flipUpDown(gameGrid)
            finalGrid = flipLeftRight(gameGrid)
    elif direction == allowedDirections[3]:
        finalGrid = flipLeftRight(gameGrid)
    else:
        finalGrid = gameGrid
    return finalGrid

def flipUpDown(gameGrid):
    flippedGrid = [0] * 16
    for i in range(16):
        flippedGrid[i] = gameGrid[15-i]
    return flippedGrid

def flipLeftRight(gameGrid):
    flippedGrid = [0] * 16
    x = 0
    for i in range(4):
        for j in range(0,13,4):
            flippedGrid[x] = gameGrid[i+j]
            x += 1
    return flippedGrid

def merge(gameGrid,score):
    for i in range(15,3,-1):
        if gameGrid[i] == gameGrid[i-4]:
            gameGrid[i] *= 2
            score += gameGrid[i]
            gameGrid[i-4] = 0
    return gameGrid, score 

def collapse(gameGrid):  
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
        