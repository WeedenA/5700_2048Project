def _shift(userParms):
    result = dict.fromkeys(['grid', 'score', 'integrity', 'status'])
    result['score'] = userParms['score']
    result['integrity'] = userParms['integrity']
    result['status'] = 'ok'
    
    
    
    gameGridList = handleInputGrid(userParms)
    print(gameGridList)
    mergedGrid = merge(gameGridList)
    print(mergedGrid)
    collapsedGrid = collapse(mergedGrid)
    print(collapsedGrid)
    finalGridString = ''.join(map(str, collapsedGrid))  
    result['grid'] = finalGridString
    return result

def handleInputGrid(inputParms):
    inputGrid = [int(i) for i in inputParms['grid']]
    print(inputGrid)
    return inputGrid

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
                gameGrid[tileAbove] = gameGrid
                isDone = False
    return gameGrid