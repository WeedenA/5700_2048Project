'''
Created on Mar 19, 2021

@author: Alex Weeden
'''
import unittest
import Tiles2048.shift as shift
from pickle import FALSE


class CreateTest(unittest.TestCase):
    def test_shift_010HappyStartingGridNoCombinesDown(self):
        expectedResult = True
        substring = '44448888'
        userParms = {'op': 'shift', 'grid': '2222222244444444', 'direction': 'down',
                     'score': '0', 'integrity': 'ASDHASHD'}
        actualResult = shift._shift(userParms)
        actualResult = actualResult['grid']
        if substring not in actualResult:
            actualResult = False
        else: 
            actualResult = True
        self.assertEqual(expectedResult, actualResult)
    
