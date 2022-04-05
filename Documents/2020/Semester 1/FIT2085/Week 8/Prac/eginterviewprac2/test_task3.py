"""
Testing file for Question 3 of Interview Prac 2

__author__ = "Maria Garcia de la Banda"
__edited__ = "Ben Di Stefano"

"""

import unittest
from army import Soldier, Archer, Cavalry, Army
from battle import Battle

class TestTask3(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.MaxDiff = None

    def tearDown(self):
        for item in self.verificationErrors:
            print(item)
        print("Number of Errors = "+str(len(self.verificationErrors)))

    def test__correct_army_given(self):
        t1 = Army()

        # Test if a (low) valid combination of unit values is accepted
        try:
            self.assertTrue(t1._Army__correct_army_given(1,1,1), msg = "Stack test 1,1,1 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test if a (high) valid combination of unit values is accepted
        try:
            self.assertTrue(t1._Army__correct_army_given(5, 5, 5), msg = "Stack test 5,5,5 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

         # Test if invalid combination of values raises error
        try:
            self.assertFalse(t1._Army__correct_army_given(5,5,6), msg = "Stack test 5,5,6 didn't fail when it should have")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        try:
            self.assertFalse(t1._Army__correct_army_given(5,5,-5), msg = "Stack test 5,5,-5 didn't fail when it should have")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test__str__(self):
        sold = "Soldier's life = 3 and experience = 0"
        arch = "Archer's life = 3 and experience = 0"
        cav = "Cavalry's life = 4 and experience = 0"
        t1 = Army()

        # Test if the string representation of the army matches expected output for low unit values
        t1._Army__assign_army("t1",1,1,1,0)
        try:
            self.assertEqual(str(t1.force), sold+","+arch+","+cav, msg = "String test 1,1,1 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test if the string representation of the army matches expected output for high unit values
        t1._Army__assign_army("t1", 2, 2, 2, 0)
        try:
            self.assertEqual(str(t1.force), sold + "," + sold + ","+ arch + "," + arch + "," + cav + "," + cav, msg="String test 2,2,2 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test if the string representation of the army matches expected output for a single fighter
        t1._Army__assign_army("t1", 1, 0, 0, 0)
        try:
            self.assertEqual(str(t1.force), sold , msg="String test 1,0,0 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test an empty string
        t1._Army__assign_army("t1", 0, 0, 0, 0)
        try:
            self.assertEqual(str(t1.force), "", msg="String test 0,0,0 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test if the string representation of the army matches expected output for an army that meets the budget
        t1._Army__assign_army("t1", 0, 0, 10, 0)
        try:
            self.assertEqual(str(t1.force), cav + "," + cav + "," + cav + "," + cav + "," + cav + "," + cav + "," + cav + "," + cav + "," + cav + "," + cav , msg="String test 0,0,10 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

if __name__ == '__main__':
    unittest.main()
