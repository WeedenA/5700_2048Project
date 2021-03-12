import unittest
import Tiles2048.create as create

class CreateTest(unittest.TestCase):

#  The following is included only for illustrative purposes.  It tests nothing
#  useful.  Please delete and replace with your own test code.
    def test_create_HappyPathTest010(self):
        userParms = {'op': 'create'}
        actualResult = create._create(userParms)
        self.assertIsNotNone(actualResult)
    def test_create_GridKeyPresent(self):
        userParms = {'op': 'create'}
        actualResult = create._create(userParms)
        self.assertIsNotNone(actualResult['grid'])
    def test_create_ScoredKeyPresent(self):
        userParms = {'op': 'create'}
        actualResult = create._create(userParms)
        self.assertIsNotNone(actualResult['score'])
    def test_create_IntegrityKeyPresent(self):
        userParms = {'op': 'create'}
        actualResult = create._create(userParms)
        self.assertIsNotNone(actualResult['Integrity'])
    def test_create_StatusKeyPresent(self):
        userParms = {'op': 'create'}
        actualResult = create._create(userParms)
        self.assertIsNotNone(actualResult['status'])
    def test_create_GridContains2StartingTiles(self):
        expectedResult = 2
        userParms = {'op': 'create'}
        actualResult = create._create(userParms)
        startingTiles = 0
        for digit in actualResult['grid']:
            if digit == '2':
                startingTiles += 1
        self.assertEqual(expectedResult, startingTiles)
    def test_create_GridStringIsCorrectLength(self):
        expectedResult = 16
        userParms = {'op': 'create'}
        actualResult = create._create(userParms)
        lengthOfGrid = len(actualResult['grid'])
        self.assertEqual(expectedResult, len(actualResult['grid']))
#     def test_create_IntegrityIsValid(self):
#         expectedResult = 999999
#         userParms = {'op': 'create'}
#         actualResult = create._create(userParms)
#         # expected result depends on starting positions
    def test_create_StatusIsOk(self):
        expectedResult = 'ok'
        userParms = {'op': 'create'}
        actualResult = create._create(userParms)
        self.assertEqual(expectedResult, actualResult['status'])
#     def test_create_StartingScoreValid(self):
#         expectedResult =  0
#         userParms = {'op': 'create'}
#         actualResult = create._create(userParms)
#         self.assertEqual(expectedResult, actualResult['score'])
#     
        