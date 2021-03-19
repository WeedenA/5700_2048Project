def _shift(userParms):
    isCaught, error = errorCheck(userParms)
    if isCaught:
        return error
    result = dict.fromkeys(['grid', 'score', 'integrity', 'status'])
    result['score'] = userParms['score']
    result['integrity'] = userParms['integrity']
    result['status'] = 'ok'
    
    chosenDirection = userParms['direction']    
    gameGridList = handleInputGrid(userParms)
    
    orientedGrid = flipDirection(gameGridList, chosenDirection, False)
    mergedGrid = merge(orientedGrid)
    collapsedGrid = collapse(mergedGrid)
    finalGrid = flipDirection(collapsedGrid, chosenDirection, True)
    print(finalGrid)
    finalGridString = ''.join(map(str, finalGrid))  
    result['grid'] = finalGridString
    return result

def errorCheck(uParms):
    requiredKeys = ['grid','score','integrity']
    error = {'status': 'ok'}
    for key in requiredKeys:
        if key not in parms:
            error['status'] = 'error - missing keys'
            return True, error
        if '0' not in parms['grid']:
            error['status'] = 'error - invalid grid'
            return True, error
        
    
    return False, error
def handleInputGrid(inputParms):
    inputGrid = [int(i) for i in inputParms['grid']]
    return inputGrid

def flipDirection(gameGrid, direction, isReverse):
    allowedDirections = ['up','down','left','right']
    finalGrid = [0]*16
    if direction == allowedDirections[0]:
        finalGrid = flipUpDown(gameGrid)
    elif direction == allowedDirections[1]:
        finalGrid = gameGrid
    elif direction == allowedDirections[2]:
        if not isReverse:
            finalGrid = flipUpDown(gameGrid)
            finalGrid = flipLeftRight(gameGrid)
        else:
            finalGrid = flipLeftRight(gameGrid)
            finalGrid = flipUpDown(gameGrid)
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

def merge(gameGrid):
    for i in range(15,3,-1):
        if gameGrid[i] == gameGrid[i-4]:
            gameGrid[i] *= 2
            gameGrid[i-4] = 0
    return gameGrid 

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