def _shift(userParms):
    result = dict.fromkeys(['grid', 'score', 'integrity', 'status'])
    result['score'] = userParms['score']
    result['integrity'] = userParms['integrity']
    result['status'] = 'ok'
    
    chosenDirection = userParms['direction']    
    gameGridList = handleInputGrid(userParms)
    orientedGrid = flipDirection(gameGridList, chosenDirection)
    mergedGrid = merge(orientedGrid)
    collapsedGrid = collapse(mergedGrid)
    finalGrid = flipDirection(collapsedGrid, chosenDirection)
    print(finalGrid)
    finalGridString = ''.join(map(str, finalGrid))  
    result['grid'] = finalGridString
    return result

def handleInputGrid(inputParms):
    inputGrid = [int(i) for i in inputParms['grid']]
    return inputGrid

def flipDirection(gameGrid, direction):
    allowedDirections = ['up','down','left','right']
    flippedGrid = [0] * 16
    if direction == allowedDirections[0]:
        for i in range(16):
            flippedGrid[i] = gameGrid[15-i]
    
    else:
        flippedGrid = gameGrid
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