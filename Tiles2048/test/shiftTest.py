'''
Created on Mar 19, 2021

@author: Alex Weeden
'''
import unittest
import Tiles2048.shift as shift
from pickle import FALSE


class CreateTest(unittest.TestCase):
    def test_shift_010HappyStartingGridNoCombinesDown(self):
        substring = '22'
        userParms = {'op': 'shift', 'grid': '0220000000000000', 'direction': 'down',
                     'score': '0', 'integrity': 'ASDHASHD'}
        actualResult = shift._shift(userParms)['grid']
        if substring not in actualResult:
            isValidGrid = False
        else: 
            isValidGrid = True
        self.assertTrue(isValidGrid)
    def test_shift_020HappyRandomGridCombinesDown(self):
        substring = '44448888'
        userParms = {'op': 'shift', 'grid': '2222222244444444', 'direction': 'down',
                     'score': '0', 'integrity': 'ASDHASHD'}
        actualResult = shift._shift(userParms)['grid']
        if substring not in actualResult:
            isValidGrid = False
        else: 
            isValidGrid = True
        self.assertTrue(isValidGrid)
    def test_shift_030HappyRandomGridCombinesUp(self):
        substring = '4444888800000000'
        userParms = {'op': 'shift', 'grid': '2222222244444444', 'direction': 'up',
                     'score': '0', 'integrity': 'ASDHASHD'}
        actualResult = shift._shift(userParms)['grid']
        if substring not in actualResult:
            isValidGrid = False
        else: 
            isValidGrid = True
        self.assertTrue(isValidGrid)
    def test_shift_040HappyRandomGridCombinesRight(self):
        substring = '0048004800480048'
        userParms = {'op': 'shift', 'grid': '2244224422442244', 'direction': 'right',
                     'score': '0', 'integrity': 'ASDHASHD'}
        actualResult = shift._shift(userParms)['grid']
        if substring not in actualResult:
            isValidGrid = False
        else: 
            isValidGrid = True
        self.assertTrue(isValidGrid)
        
    
    def test_shift_110SadNoGridGiven(self):
        expectedResult = {'status': 'error - missing keys'}
        userParms = {'op': 'shift', 'direction': 'right',
                     'score': '0', 'integrity': 'ASDHASHD'}
        actualResult = shift._shift(userParms)
        self.assertEqual(expectedResult, actualResult)
    def test_shift_110SadNoScoreGiven(self):
        expectedResult = {'status': 'error - missing keys'}
        userParms = {'op': 'shift', 'grid': '2244224422442244', 'direction': 'right',
                      'integrity': 'ASDHASHD'}
        actualResult = shift._shift(userParms)
        self.assertEqual(expectedResult, actualResult)
         