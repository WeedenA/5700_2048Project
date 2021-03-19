'''
Created on Mar 19, 2021

@author: Alex Weeden
'''
import unittest
import Tiles2048.shift as shift


class CreateTest(unittest.TestCase):
    def test_shift_010HappyStartingGridNoCombinesDown(self):
        expectedResult = '0000000044448888'
        userParms = {'op': 'shift', 'grid': '2222222244444444', 'direction': 'down',
                     'score': '0', 'integrity': 'ASDHASHD'}
        actualResult = shift._shift(userParms)
        actualResult = actualResult['grid']
        self.assertEqual(expectedResult, actualResult)
    
