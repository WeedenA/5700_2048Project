def _shift(userParms):
    isCaught, error = errorCheck(userParms)
    if isCaught:
        return error
    result = dict.fromkeys(['grid', 'score', 'integrity', 'status'])
    result['score'] = userParms['score']
    result['integrity'] = userParms['integrity']
    result['status'] = 'ok'
    
    if 'direction' not in userParms:
        userParms['direction'] = 'down'
    chosenDirection = userParms['direction']
        
    gameGridList, isErrorFound = handleInputGrid(userParms['grid'])
    if isErrorFound:
        return {'status': 'error - invalid grid'}
    
    orientedGrid = flipDirection(gameGridList, chosenDirection, False)
    combinedGrid = combine(orientedGrid)
    finalGrid = flipDirection(combinedGrid, chosenDirection, True) 
    
    finalGridString = ''.join(map(str, finalGrid))  
    result['grid'] = finalGridString
    return result

def errorCheck(parms):
    requiredKeys = ['grid','score','integrity']
    error = {'status': 'ok'}
    for key in requiredKeys:
        if key not in parms:
            error['status'] = 'error - missing keys'
            return True, error
    if '0' not in parms['grid']:
        error['status'] = 'error - no moves available'
        return True, error
    if int(parms['score']) % 2 != 0:
        error['status'] = 'error - invalid score'
        return True, error
        
    return False, error
def combine(grid):
    collapse(grid)
    merge(grid)
    collapse(grid)
    return grid
    

def handleInputGrid(grid):
    x = 0
    inputGrid = [0] * 16
    
    #todo: dear god figure something out for this
    for i in range(16):
        try:
            testIndex = grid[x]
        except IndexError:
            return grid, True
        if grid[x] == '0':
            inputGrid[i] = 0
            x += 1
            continue
        elif grid[x] == '1':
            if grid[x:x+4] == '1024':
                inputGrid[i] = 1024
                x+=4
                continue
            elif grid[x:x+3] == '128':
                inputGrid[i] == 128
                x+=3
                continue
            elif grid[x:x+2] == '16':
                inputGrid[i] = 16
                x+=2
                continue
            else:
                return inputGrid, True
        elif grid[x] == '2':
            if grid[x:x+3] == '256':
                inputGrid[i] = 256
                x+=2
                continue
            else: 
                inputGrid[i] = 2
                x+=1
                continue
        elif grid[x] == '4':
            inputGrid[i] = 4
            x+=1
            continue
        elif grid[x] == '8':
            inputGrid[i] = 8
            x+=1
            continue
        elif grid[x:x+2] == '32':
            inputGrid[i] = 32
            x+=2
            continue
        elif grid[x:x+2] == '64':
            inputGrid[i] = 64
            x+=2
            continue
        elif grid[x:x+3] == '512':
            inputGrid[i] = 512
            x+=2
            continue
        else:
            return inputGrid, True
    try:
        testIndex = grid[x]
    except IndexError:
        return inputGrid, False
    return inputGrid, True

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