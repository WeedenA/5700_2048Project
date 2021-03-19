def _shift(userParms):
    result = dict.fromkeys(['grid', 'score', 'Integrity', 'status'])
    
    gameGridList = handleInputGrid(userParms)
    
    mergedGrid = merge(gameGridList)
    collapsedGrid = collapse(mergedGrid)
    
    
#     
#     inputGrid = userParms['grid']
#     gameGridList = [0] * 16
#     for i in range(len(inputGrid)):
#         gameGridList[i] = inputGrid[i]
    
    
    
    
    
    
    
    
    return collapsedGrid

def handleInputGrid(inputParms):
    inputGrid = []
    inputGrid[:0] = inputParms['grid']
    for i in range(len(inputGrid)):
        inputGrid[i] = int(inputGrid[i])
    return inputGrid

def merge(gameGrid):
    for i in range(15,3,-1):
        if gameGrid[i] == gameGrid[i-4]:
            gameGrid[i] *= 2
            gameGrid[i-4] = 0
    return gameGrid 

def collapse(gameGrid):
    for i in range(15,3,-1):
        if gameGrid[i] == 0 and gameGrid[i-4] != 0:
            gameGrid[i] = gameGrid[i-4]
            gameGrid[i-4] = gameGrid