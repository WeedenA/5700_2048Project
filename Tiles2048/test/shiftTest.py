'''
Created on Mar 19, 2021

@author: Alex Weeden
'''
import unittest
import Tiles2048.shift as shift


class CreateTest(unittest.TestCase):
    def test_shift_010HappyStartingGridNoCombinesDown(self):
        expectedResult = {'grid': '0000000000002200', 'score': '0', 'integrity': 'ASDHASHD', 
                          'status': 'ok'}
        userParms = {'op': 'shift', 'grid': '2222000000000000', 'direction': 'down',
                     'score': '0', 'integrity': 'ASDHASHD'}
        actualResult = shift._shift(userParms)
        self.assertEqual(expectedResult, actualResult)
    
