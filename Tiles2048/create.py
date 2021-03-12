import random.randint
def _create(userParms):
    result = dict.fromkeys(['grid', 'score', 'Integrity', 'status'])
    result['grid'] = '0'
    gridWidth = 4 # predetermined by game ruleset
    gridHeight = 4 # predetermined by game ruleset
    totalGridTiles = gridWidth * gridHeight
    gameGridList = [0] * totalGridTiles
        
    gameGridString = ''
    for value in gameGridList:
        gameGridString += str(value)
    result['grid'] = gameGridString
    
    
    
    
    
    result['score'] = 0
    result['Integrity'] = 'somehashthing'
    result['status'] = 'pass/fail' 
    return result
