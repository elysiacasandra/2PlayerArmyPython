"""
Testing file for Question 4 of Interview Prac 2

__author__ = "Maria Garcia de la Banda"
__edited__ = "Ben Di Stefano"

"""

import unittest
from army import Archer, Soldier, Cavalry, Army
from battle import Battle


class TestTask4(unittest.TestCase):

    def setUp(self):
        self.verificationErrors = []

    def tearDown(self):
        for item in self.verificationErrors:
            print(item)
        print("Number of Errors = "+str(len(self.verificationErrors)))

    def test___conduct_combat(self):
        t1 = Army()
        t2 = Army()
        battle = Battle()
        formation = 0

        # Tests where player 2 should win
        # Test if combat is conducted correctly and returns appropriate result for empty p1 army and all Archer p2 army
        # Assumes __assign_army is working correctly
        t1._Army__assign_army("", 0, 0, 0, formation)
        t2._Army__assign_army("", 0, 10, 0, formation)
        try:
            self.assertTrue(battle._Battle__conduct_combat(t1, t2, formation) == 2, "Gladiatorial 0,0,0 0,10,0 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test if combat is conducted correctly and returns appropriate result for 3,2,2 and 5,4,1
        # Assumes __assign_army is working correctly
        t1._Army__assign_army("", 3, 2, 2, formation)
        t2._Army__assign_army("", 5, 4, 1, formation)
        try:
            self.assertTrue(battle._Battle__conduct_combat(t1, t2, formation) == 2,"Gladiatorial 3,2,2 5,4,1 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Tests where player 1 should win
        # Test if combat is conducted correctly and returns appropriate result player 1 with an archer and player 2 with a soldier
        # Assumes __assign_army is working correctly
        t1._Army__assign_army("", 4, 4, 3, formation)
        t2._Army__assign_army("", 3, 3, 2, formation)
        try:
            self.assertTrue(battle._Battle__conduct_combat(t1, t2, formation) == 1,"Gladiatorial 4,4,3 3,3,2 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test if combat is conducted correctly and returns appropriate result player 1 with cavalry and player 2 with an archer
        # Assumes __assign_army is working correctly
        t1._Army__assign_army("", 0, 0, 3, formation)
        t2._Army__assign_army("", 0, 0, 2, formation)
        try:
            self.assertTrue(battle._Battle__conduct_combat(t1, t2, formation) == 1,"Gladiatorial 0,0,3 0,0,2 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Tests where the players should draw
        # Test if combat is conducted correctly and returns appropriate result for army with the same type and number of fighters
        # Assumes __assign_army is working correctly
        t1._Army__assign_army("", 1, 1, 1, formation)
        t2._Army__assign_army("", 1, 1, 1, formation)
        try:
            self.assertTrue(battle._Battle__conduct_combat(t1, t2, formation) == 0, "Gladiatorial 1,1,1 1,1,1 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test if combat is conducted correctly and returns appropriate result for army with empty armys
        # Assumes __assign_army is working correctly
        t1._Army__assign_army("", 0, 0, 0, formation)
        t2._Army__assign_army("", 0, 0, 0, formation)
        try:
            self.assertTrue(battle._Battle__conduct_combat(t1, t2, formation) == 0, "Gladiatorial 0,0,0 0,0,0 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))



if __name__ == '__main__':
    unittest.main()
