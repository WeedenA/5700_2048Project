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
    



