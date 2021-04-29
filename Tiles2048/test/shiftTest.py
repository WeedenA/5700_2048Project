'''
Created on Mar 19, 2021

@author: Alex Weeden
'''
import unittest
import Tiles2048.shift as shift

INTEGRITY = '1FE1E3C4A3BB3616AFE46B941941D629F7C53F78F3336FEB311F64DF7747C672'

def compareGrids(grid, expectedGrid):
    if (len(grid) != len(expectedGrid)):
        return False
    diff = 0
    for charIndex in range(len(grid)):
        if grid[charIndex] != expectedGrid[charIndex]:
            diff += 1
            if (diff > 1):
                return False
    return True
    
class CreateTest(unittest.TestCase):
    def test_shift_010HappyStartingGridNoCombinesDown(self):
        expectedResult = '0000000000000220'
        userParms = {'op': 'shift', 'grid': '0220000000000000', 'direction': 'down',
                     'score': '0', 'integrity': INTEGRITY}
        actualResult = shift._shift(userParms)['grid']
        isValidGrid = compareGrids(expectedResult, actualResult)
        self.assertTrue(isValidGrid)
    def test_shift_020HappyRandomGridCombinesDown(self):
        expectedResult = '000000080032848648'
        userParms = {'op': 'shift', 'grid': '00168241640432420328', 'direction': 'down',
                     'score': '0', 'integrity': INTEGRITY}
        actualResult = shift._shift(userParms)['grid']
        isValidGrid = compareGrids(expectedResult, actualResult)
        self.assertTrue(isValidGrid)
    def test_shift_030HappyRandomGridCombinesUp(self):
        expectedResult = '483280064800080000'
        userParms = {'op': 'shift', 'grid': '00168241640432420328', 'direction': 'up',
                     'score': '0', 'integrity': INTEGRITY}
        actualResult = shift._shift(userParms)['grid']
        isValidGrid = compareGrids(expectedResult, actualResult)
        self.assertTrue(isValidGrid)
    def test_shift_040HappyRandomGridCombinesRight(self):
        expectedResult = '000400080032640888'
        userParms = {'op': 'shift', 'grid': '02020440161632328448', 'direction': 'right',
                     'score': '0', 'integrity': INTEGRITY}
        actualResult = shift._shift(userParms)['grid']
        isValidGrid = compareGrids(expectedResult, actualResult)
        self.assertTrue(isValidGrid)
    def test_shift_050HappyRandomGridCombinesLeft(self):
        expectedResult = '400080003264008880'
        userParms = {'op': 'shift', 'grid': '02020440161632328448', 'direction': 'left',
                     'score': '0', 'integrity': INTEGRITY}
        actualResult = shift._shift(userParms)['grid']
        isValidGrid = compareGrids(expectedResult, actualResult)
        self.assertTrue(isValidGrid)
    def test_shift_060HappyRandomGridNoDirectionChoice(self):
        expectedResult = '000000080032848648'
        userParms = {'op': 'shift', 'grid': '00168241640432420328',
                     'score': '0', 'integrity': INTEGRITY}
        actualResult = shift._shift(userParms)['grid']
        isValidGrid = compareGrids(expectedResult, actualResult)
        self.assertTrue(isValidGrid)  
    def test_shift_061HappyRandomGridNoDirectionChoice(self):
        expectedResult = '000000080032848648'
        userParms = {'op': 'shift', 'grid': '00168241640432420328', 'direction': '',
                     'score': '0', 'integrity': INTEGRITY}
        actualResult = shift._shift(userParms)['grid']
        isValidGrid = compareGrids(expectedResult, actualResult)
        self.assertTrue(isValidGrid)  
    def test_shift_062HappyRandomGridMixedDirectionChoice(self):
        expectedResult = '000000080032848648'
        userParms = {'op': 'shift', 'grid': '00168241640432420328', 'direction': 'DoWn',
                     'score': '0', 'integrity': INTEGRITY}
        actualResult = shift._shift(userParms)['grid']
        isValidGrid = compareGrids(expectedResult, actualResult)
        self.assertTrue(isValidGrid)
    def test_shift_070HappyStartingGridBiggerNumbers(self):
        expectedResult = '000000000320003200'
        userParms = {'op': 'shift', 'grid': '01600016000160001600', 'direction': 'down',
                     'score': '0', 'integrity': INTEGRITY}
        actualResult = shift._shift(userParms)['grid']
        isValidGrid = compareGrids(expectedResult, actualResult)
        self.assertTrue(isValidGrid)
    def test_shift_080HappyWinningRound(self):
        expectedResult = 'win'
        userParms = {'op': 'shift', 'grid': '0000000010240001024000', 'direction': 'down',
                     'score': '0', 'integrity': INTEGRITY}
        actualResult = shift._shift(userParms)['status']
        self.assertEqual(expectedResult, actualResult)
    def test_shift_090HappyLosingRound(self):
        expectedResult = 'lose'
        userParms = {'op': 'shift', 'grid': '022232323232888816161616', 'direction': 'down',
                     'score': '0', 'integrity': INTEGRITY}
        actualResult = shift._shift(userParms)['status']
        self.assertEqual(expectedResult, actualResult)
    def test_shift_100HappyExtraneousParmsGiven(self):
        expectedResult = '400080003264008880'
        userParms = {'op': 'shift', 'grid': '02020440161632328448', 'direction': 'left',
                     'score': '0', 'integrity': INTEGRITY, 'randomKey': 'randomValue'}
        actualResult = shift._shift(userParms)['grid']
        isValidGrid = compareGrids(expectedResult, actualResult)
        self.assertTrue(isValidGrid)
    def test_shift_110HappyScoreCalculated(self):
        expectedResult = '16'
        userParms = {'op': 'shift', 'grid': '2200202020022200', 'direction': 'left',
                     'score': '0', 'integrity': INTEGRITY}
        actualResult = shift._shift(userParms)['score']
        self.assertEqual(expectedResult, actualResult)
    def test_shift_120HappyFullGridButStillOKStatus(self):
        expectedResult = '0000000044448888'
        userParms = {'op': 'shift', 'grid': '2222222244444444', 'direction': 'down',
                     'score': '0', 'integrity': INTEGRITY}
        actualResult = shift._shift(userParms)['grid']
        isValidGrid = compareGrids(expectedResult, actualResult)
        self.assertTrue(isValidGrid)
    def test_shift_120HappyFullGridAfterShiftAddButStillOKStatus(self):
        expectedResult = 'ok'
        userParms = {'op': 'shift', 'grid': '24816232643241632646481632', 'direction': 'down',
                     'score': '0', 'integrity': INTEGRITY}
        actualResult = shift._shift(userParms)['status']
        self.assertEqual(expectedResult, actualResult)  
     
    def test_shift_210SadNoGridGiven(self):
        expectedResult = {'status': 'error - missing grid'}
        userParms = {'op': 'shift', 'direction': 'right',
                     'score': '0', 'integrity': INTEGRITY}
        actualResult = shift._shift(userParms)
        self.assertEqual(expectedResult, actualResult)
    def test_shift_220SadNoScoreGiven(self):
        expectedResult = {'status': 'error - missing score'}
        userParms = {'op': 'shift', 'grid': '0044224422442244', 'direction': 'right',
                     'integrity': INTEGRITY}
        actualResult = shift._shift(userParms)
        self.assertEqual(expectedResult, actualResult)
    def test_shift_221SadEmptyScoreGiven(self):
        expectedResult = {'status': 'error - missing score'}
        userParms = {'op': 'shift', 'grid': '0044224422442244', 'direction': 'right',
                     'score': '','integrity': INTEGRITY}
        actualResult = shift._shift(userParms)
        self.assertEqual(expectedResult, actualResult)
    def test_shift_230SadNoMovesAvailable(self):
        expectedResult = {'status': 'error - no shift possible'}
        userParms = {'op': 'shift', 'grid': '2481632641283224816326412832', 'score': '0', 'direction': 'right',
                      'integrity': INTEGRITY}
        actualResult = shift._shift(userParms)
        self.assertEqual(expectedResult, actualResult)
    def test_shift_240SadInvalidScore(self):
        expectedResult = {'status': 'error - invalid score'}
        userParms = {'op': 'shift', 'grid': '0044224422442244', 'score': '59', 'direction': 'right',
                      'integrity': INTEGRITY}
        actualResult = shift._shift(userParms)
        self.assertEqual(expectedResult, actualResult)
    def test_shift_250SadGridTooShort(self):
        expectedResult = {'status': 'error - invalid grid'}
        userParms = {'op': 'shift', 'grid': '000222', 'direction': 'right',
                     'score': '0', 'integrity': INTEGRITY}
        actualResult = shift._shift(userParms)
        self.assertEqual(expectedResult, actualResult)
    def test_shift_260SadGridTooLong(self):
        expectedResult = {'status': 'error - invalid grid'}
        userParms = {'op': 'shift', 'grid': '000000000000000000', 'direction': 'right',
                     'score': '0', 'integrity': INTEGRITY}
        actualResult = shift._shift(userParms)
        self.assertEqual(expectedResult, actualResult)
    def test_shift_280SadInvalidNumbersInGrid(self):
        expectedResult = {'status': 'error - invalid grid'}
        userParms = {'op': 'shift', 'grid': '7245000000000000', 'direction': 'right',
                     'score': '0', 'integrity': INTEGRITY}
        actualResult = shift._shift(userParms)
        self.assertEqual(expectedResult, actualResult)
    def test_shift_290SadInvalidDirectionGiven(self):
        expectedResult = {'status': 'error - invalid direction'}
        userParms = {'op': 'shift', 'grid': '0000000000000000', 'direction': 'toTheWindow',
                     'score': '0', 'integrity': INTEGRITY}
        actualResult = shift._shift(userParms)
        self.assertEqual(expectedResult, actualResult)
    def test_shift_300SadInvalidIntegrityGiven(self):
        expectedResult = {'status': 'error - invalid integrity'}
        userParms = {'op': 'shift', 'grid': '0000000000000000', 'direction': 'down',
                     'score': '0', 'integrity': 'RESPECTFINDOUTWHATITMEANSTOME'}
        actualResult = shift._shift(userParms)
        self.assertEqual(expectedResult, actualResult)
    def test_shift_310SadNonIntScoreGiven(self):
        expectedResult = {'status': 'error - non-int score'}
        userParms = {'op': 'shift', 'grid': '0000000000000000', 'direction': 'down',
                     'score': 'a', 'integrity': INTEGRITY}
        actualResult = shift._shift(userParms)
        self.assertEqual(expectedResult, actualResult)
    def test_shift_310SadOOBScoreGiven(self):
        expectedResult = {'status': 'error - out of bounds score'}
        userParms = {'op': 'shift', 'grid': '0000000000000000', 'direction': 'down',
                     'score': '-50', 'integrity': INTEGRITY}
        actualResult = shift._shift(userParms)
        self.assertEqual(expectedResult, actualResult)
    def test_shift_301SadInvalidIntegrityGiven(self):
        expectedResult = {'status': 'error - invalid integrity'}
        userParms = {'op': 'shift', 'grid': '0000000000000000', 'direction': 'down',
                     'score': '0', 'integrity': '1FE1E3C4A3BB3616AFE46B941941D629F7C53F78F3336FEB311F64DF7747Q672'}
        actualResult = shift._shift(userParms)
        self.assertEqual(expectedResult, actualResult)
          