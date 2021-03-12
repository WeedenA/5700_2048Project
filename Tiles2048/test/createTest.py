import unittest
import Tiles2048.create as create

class CreateTest(unittest.TestCase):

#  The following is included only for illustrative purposes.  It tests nothing
#  useful.  Please delete and replace with your own test code.
    def test_create_HappyPathTest010(self):
        userParms = {'op': 'create'}
        actualResult = create._create(userParms)
        self.assertIsNotNone(actualResult)
    def test_create_HappyPathStringUnderGrid(self):
        expectedResult = {'create': 'create stub'}
        userParms = {'op': 'create'}
        actualResult = create._create(userParms)
        self.assertDictEqual(expectedResult, actualResult)
    