"""
Testing file for Question 5 of Interview Prac 2

__author__ = "Maria Garcia de la Banda"
__edited__ = "Ben Di Stefano"

"""

import unittest
from army import Archer, Soldier, Cavalry, Army
from battle import Battle


class TestTask5(unittest.TestCase):

    def setUp(self):
        self.verificationErrors = []

    def tearDown(self):
        for item in self.verificationErrors:
            print(item)
        print("Number of Errors = "+str(len(self.verificationErrors)))

    def test__conduct_combat(self):
        t1 = Army()
        t2 = Army()
        battle = Battle()
        formation = 1

        # Test if combat is conducted correctly and if it returns
        # appropriate result for all Archer p1 army and empty p2 army
        # Assumes __assign_army is working correctly
        t1._Army__assign_army("", 0, 10, 0, formation)
        t2._Army__assign_army("", 0, 0, 0, formation)
        try:
            self.assertTrue(battle._Battle__conduct_combat(t1, t2, formation) == 1, "Fairer 0,10,0 0,0,0 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Tests combat is conducted correctly and if it
        # returns appropriate result for 1 Soldier p1 army and 1 Archer p2 army
        # Assumes __assign_army is working correctly
        t1._Army__assign_army("", 1, 0, 0, formation)
        t2._Army__assign_army("", 0, 1, 0, formation)
        try:
            self.assertTrue(battle._Battle__conduct_combat(t1, t2, formation) == 2, "Fairer 1,0,0 0,1,0 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertEqual(str(t1.force),"", msg="Army 1 wrong for Fairer 1,0,0 0,1,0")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertEqual(str(t2.force), "Archer's life = 1 and experience = 1", msg="Army 2 wrong for Fairer 1,0,0 0")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test if combat is conducted correctly and returns appropriate result for empty p1 army and all Archer p2 army
        # Assumes __assign_army is working correctly
        t1._Army__assign_army("", 0, 0, 0, formation)
        t2._Army__assign_army("", 0, 1, 0, formation)
        try:
            self.assertTrue(battle._Battle__conduct_combat(t1, t2, formation) == 2, "Gladiatorial 0,0,0 0,10,0 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertEqual(str(t1.force),"", msg="Army 1 wrong for Fairer 0,0,0 0,2,0")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertEqual(str(t2.force), "Archer's life = 3 and experience = 0", msg="Army 2 wrong for Fairer 0,0,0 0,10,0")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test if combat is conducted correctly and returns appropriate result for 3,2,2 and 2,3,1
        # Assumes __assign_army is working correctly
        t1._Army__assign_army("", 3, 2, 2, formation)
        t2._Army__assign_army("", 2, 3, 1, formation)
        try:
            self.assertTrue(battle._Battle__conduct_combat(t1, t2, formation) == 1,"Gladiatorial 3,2,2 2,3,1 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertEqual(str(t1.force),"Cavalry's life = 3 and experience = 2", msg="Army 1 wrong for Fairer 3,2,2 2,3,1")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertEqual(str(t2.force), "", msg="Army 2 wrong for Fairer 3,2,2 2,3,1")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test if combat is conducted correctly and returns appropriate result player 1 with an archer and player 2 with a soldier
        # Assumes __assign_army is working correctly
        t1._Army__assign_army("", 2, 2, 3, formation)
        t2._Army__assign_army("", 3, 3, 2, formation)
        try:
            self.assertTrue(battle._Battle__conduct_combat(t1, t2, formation) == 2,"Gladiatorial 2,2,3 3,3,2 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertEqual(str(t1.force),"", msg="Army 1 wrong for Fairer 2,2,3 3,3,2")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertEqual(str(t2.force), "Cavalry's life = 1 and experience = 4", msg="Army 2 wrong for Fairer 3,2,2 2,3,1")
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
        try:
            self.assertEqual(str(t1.force),"Cavalry's life = 2 and experience = 0,Cavalry's life = 2 and experience = 1", msg="Army 1 wrong for Fairer 0,0,3 0,0,2")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertEqual(str(t2.force), "", msg="Army 2 wrong for Fairer 0,0,3 0,0,2")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test if combat is conducted correctly and returns appropriate result for army with the same type and number of fighters
        # Assumes __assign_army is working correctly
        t1._Army__assign_army("", 1, 1, 1, formation)
        t2._Army__assign_army("", 1, 1, 1, formation)
        try:
            self.assertTrue(battle._Battle__conduct_combat(t1, t2, formation) == 0, "Gladiatorial 1,1,1 1,1,1 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertEqual(str(t1.force),"", msg="Army 1 wrong for Fairer 1,1,1 1,1,1")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertEqual(str(t2.force), "", msg="Army 2 wrong for Fairer 1,1,1 1,1,1")
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
        try:
            self.assertEqual(str(t1.force),"", msg="Army 1 wrong for Fairer 0,0,0 0,0,0")
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertEqual(str(t2.force), "", msg="Army 2 wrong for Fairer 0,0,0 0,0,0")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

if __name__ == '__main__':
  unittest.main()
