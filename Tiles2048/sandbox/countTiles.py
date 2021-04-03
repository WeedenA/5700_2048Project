'''
Created on Mar 12, 2021

@author: Alex Weeden
'''
{'status': 'error: bad shit'}

def assessRound(parms, grid):
    if 2048 in grid:
        return 'win'
    if 0 not in grid:
        return 'lose'
    return 'ok'

for x in range(4):
    


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
                
                




def handleInputGrid(grid):
    parseIndex = 0
    inputGrid = [0] * 16
    
    #todo: dear god figure something out for this
    for tile in range(16):
        try:
            grid[parseIndex]
        except IndexError:
            return grid, True
        if grid[parseIndex] == '0':
            inputGrid[tile] = 0
            parseIndex += 1
            continue
        elif grid[parseIndex] == '1':
            if grid[parseIndex:parseIndex+4] == '1024':
                inputGrid[tile] = 1024
                parseIndex+=4
                continue
            elif grid[parseIndex:parseIndex+3] == '128':
                inputGrid[tile] == 128
                parseIndex+=3
                continue
            elif grid[parseIndex:parseIndex+2] == '16':
                inputGrid[tile] = 16
                parseIndex+=2
                continue
            else:
                return inputGrid, True
        elif grid[parseIndex] == '2':
            if grid[parseIndex:parseIndex+3] == '256':
                inputGrid[tile] = 256
                parseIndex+=2
                continue
            else: 
                inputGrid[tile] = 2
                parseIndex+=1
                continue
        elif grid[parseIndex] == '4':
            inputGrid[tile] = 4
            parseIndex+=1
            continue
        elif grid[parseIndex] == '8':
            inputGrid[tile] = 8
            parseIndex+=1
            continue
        elif grid[parseIndex:parseIndex+2] == '32':
            inputGrid[tile] = 32
            parseIndex+=2
            continue
        elif grid[parseIndex:parseIndex+2] == '64':
            inputGrid[tile] = 64
            parseIndex+=2
            continue
        elif grid[parseIndex:parseIndex+3] == '512':
            inputGrid[tile] = 512
            parseIndex+=2
            continue
        else:
            return inputGrid, True
    try:
        grid[parseIndex]
    except IndexError:
        return inputGrid, False
    return inputGrid, True
