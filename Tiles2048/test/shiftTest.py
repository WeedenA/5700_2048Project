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
        substring = '444'
        userParms = {'op': 'shift', 'grid': '2220222044404440', 'direction': 'down',
                     'score': '0', 'integrity': 'ASDHASHD'}
        actualResult = shift._shift(userParms)['grid']
        if substring not in actualResult:
            isValidGrid = False
        else: 
            isValidGrid = True
        self.assertTrue(isValidGrid)
    def test_shift_030HappyRandomGridCombinesUp(self):
        substring = '888'
        userParms = {'op': 'shift', 'grid': '0222022244444444', 'direction': 'up',
                     'score': '0', 'integrity': 'ASDHASHD'}
        actualResult = shift._shift(userParms)['grid']
        if substring not in actualResult:
            isValidGrid = False
        else: 
            isValidGrid = True
        self.assertTrue(isValidGrid)
    def test_shift_040HappyRandomGridCombinesRight(self):
        substring = '4800'
        userParms = {'op': 'shift', 'grid': '0000224422442244', 'direction': 'right',
                     'score': '0', 'integrity': 'ASDHASHD'}
        actualResult = shift._shift(userParms)['grid']
        if substring not in actualResult:
            isValidGrid = False
        else: 
            isValidGrid = True
        self.assertTrue(isValidGrid)
    def test_shift_050HappyRandomGridCombinesLeft(self):
        substring = '40004000'
        userParms = {'op': 'shift', 'grid': '2200202020022200', 'direction': 'left',
                     'score': '0', 'integrity': 'ASDHASHD'}
        actualResult = shift._shift(userParms)['grid']
        if substring not in actualResult:
            isValidGrid = False
        else: 
            isValidGrid = True
        self.assertTrue(isValidGrid)
    def test_shift_060HappyDefaultDirection(self):
        substring = '888'
        userParms = {'op': 'shift', 'grid': '2220222044404440',
                     'score': '0', 'integrity': 'ASDHASHD'}
        actualResult = shift._shift(userParms)['grid']
        if substring not in actualResult:
            isValidGrid = False
        else: 
            isValidGrid = True
        self.assertTrue(isValidGrid)    
    def test_shift_070HappyStartingGridBiggerNumbers(self):
        substring = '32'
        userParms = {'op': 'shift', 'grid': '01600016000160001600', 'direction': 'down',
                     'score': '0', 'integrity': 'ASDHASHD'}
        actualResult = shift._shift(userParms)['grid']
        if substring not in actualResult:
            isValidGrid = False
        else: 
            isValidGrid = True
        self.assertTrue(isValidGrid)
    def test_shift_080HappyWinningRound(self):
        expectedResult = 'win'
        userParms = {'op': 'shift', 'grid': '0000000010240001024000', 'direction': 'down',
                     'score': '0', 'integrity': 'ASDHASHD'}
        actualResult = shift._shift(userParms)['status']
        self.assertEqual(expectedResult, actualResult)
    def test_shift_090HappyLosingRound(self):
        expectedResult = 'lose'
        userParms = {'op': 'shift', 'grid': '02224444888816161616', 'direction': 'down',
                     'score': '0', 'integrity': 'ASDHASHD'}
        actualResult = shift._shift(userParms)['status']
        self.assertEqual(expectedResult, actualResult)
    def test_shift_100ExtraneousParmsGiven(self):
        substring = '40004000'
        userParms = {'op': 'shift', 'grid': '2200202020022200', 'direction': 'left',
                     'score': '0', 'integrity': 'ASDHASHD', 'randomKey': 'randomValue'}
        actualResult = shift._shift(userParms)['grid']
        if substring not in actualResult:
            isValidGrid = False
        else: 
            isValidGrid = True
        self.assertTrue(isValidGrid)
    def test_shift_110HappyScoreCalculated(self):
        expectedResult = '16'
        userParms = {'op': 'shift', 'grid': '2200202020022200', 'direction': 'left',
                     'score': '0', 'integrity': 'ASDHASHD'}
        actualResult = int(shift._shift(userParms)['score'])
         
        self.assertEqual(expectedResult, actualResult)
    
    def test_shift_210SadNoGridGiven(self):
        expectedResult = {'status': 'error - missing keys'}
        userParms = {'op': 'shift', 'direction': 'right',
                     'score': '0', 'integrity': 'ASDHASHD'}
        actualResult = shift._shift(userParms)
        self.assertEqual(expectedResult, actualResult)
    def test_shift_220SadNoScoreGiven(self):
        expectedResult = {'status': 'error - missing keys'}
        userParms = {'op': 'shift', 'grid': '0044224422442244', 'direction': 'right',
                     'integrity': 'ASDHASHD'}
        actualResult = shift._shift(userParms)
        self.assertEqual(expectedResult, actualResult)
    def test_shift_230SadFullGrid(self):
        expectedResult = {'status': 'error - no moves available'}
        userParms = {'op': 'shift', 'grid': '2244224422442244', 'score': '0', 'direction': 'right',
                      'integrity': 'ASDHASHD'}
        actualResult = shift._shift(userParms)
        self.assertEqual(expectedResult, actualResult)
    def test_shift_240SadInvalidScore(self):
        expectedResult = {'status': 'error - invalid score'}
        userParms = {'op': 'shift', 'grid': '0044224422442244', 'score': '59', 'direction': 'right',
                      'integrity': 'ASDHASHD'}
        actualResult = shift._shift(userParms)
        self.assertEqual(expectedResult, actualResult)
    def test_shift_250GridTooShort(self):
        expectedResult = {'status': 'error - invalid grid'}
        userParms = {'op': 'shift', 'grid': '000222', 'direction': 'right',
                     'score': '0', 'integrity': 'ASDHASHD'}
        actualResult = shift._shift(userParms)
        self.assertEqual(expectedResult, actualResult)
    def test_shift_260GridTooLong(self):
        expectedResult = {'status': 'error - invalid grid'}
        userParms = {'op': 'shift', 'grid': '000000000000000000', 'direction': 'right',
                     'score': '0', 'integrity': 'ASDHASHD'}
        actualResult = shift._shift(userParms)
        self.assertEqual(expectedResult, actualResult)
    def test_shift_280InvalidNumbersInGrid(self):
        expectedResult = {'status': 'error - invalid grid'}
        userParms = {'op': 'shift', 'grid': '7245000000000000', 'direction': 'right',
                     'score': '0', 'integrity': 'ASDHASHD'}
        actualResult = shift._shift(userParms)
        self.assertEqual(expectedResult, actualResult)
    def test_shift_290InvalidDirectionGiven(self):
        expectedResult = {'status': 'error - invalid direction'}
        userParms = {'op': 'shift', 'grid': '0000000000000000', 'direction': 'toTheWindow',
                     'score': '0', 'integrity': 'ASDHASHD'}
        actualResult = shift._shift(userParms)
        self.assertEqual(expectedResult, actualResult)
         