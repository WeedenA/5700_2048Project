def _create(userParms):
    result = dict.fromkeys(['grid', 'score', 'Integrity', 'status'])
    result['grid'] = '0'
    gridWidth = 4 # predetermined by game ruleset
    gridHeight = 4 # predetermined by game ruleset
    totalGridTiles = gridWidth * gridHeight
    startingGridList = [0] * totalGridTiles
    startingGridString = ''
    for value in startingGridList:
        startingGridString += str(value)
    result['grid'] = startingGridString
    result['score'] = 0
    result['Integrity'] = 'somehashthing'
    result['status'] = 'pass/fail' 
    return result
