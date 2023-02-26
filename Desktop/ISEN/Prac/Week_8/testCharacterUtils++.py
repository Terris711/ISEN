from CharacterUtilsFixed import charCase

import unittest

class CharacterUtilsTest(unittest.TestCase):

    def testcharCase(self):
        print("Run 1")
        self.assertEqual(charCase(True, "A"),1, "Checkupper is True and Ch is uppercase")

        assertIsNot(charCase(True, "a"),1,"Checkupper is true and Ch is lowercase")

    def testsubstr(self):
        print("Run 2")
        self.assertEqual(substr(str1,str2),str1 ,"String 1 is in string 2")
        self.assertEqual(substr(str1,str2),str2 ,"String 2 is in string 1")

