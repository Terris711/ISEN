from HealthCalc import uvRating
import unittest

class HealthCalcTest(unittest.TestCase):

    def testHealthCalc(self):
        print("Test 1")
        self.assertEqual(uvRating(-1), "-", "index < 0") 
    
        self.assertEqual(uvRating(2),"low", "0 <= index < 3")
    
        self.assertEqual(uvRating(5),"moderate", "3 <= index < 6") 
    
        self.assertEqual(uvRating(7),"high", "6 <= index < 8") 
    
        self.assertEqual(uvRating(9),"very high", "8 <= index < 11") 
    
        self.assertEqual(uvRating(13),"extreme", "index > 11")

    def testHealthCalcBVA():
        print("Test 2")
        self.assertEqual(uvRating(-0.0001), "-", "Invalid/0")
        self.assertEqual(uvRating(2.999999),"low", "2.999999/3")

        self.assertEqual(uvRating(2.999999), "low", "2.999999/3")
        self.assertEqual(uvRating(3), "moderate", "2.999999/3")
    
        self.assertEqual(uvRating(5.999999),"moderate", "5.999999/6")
        self.assertEqual(uvRating(6),"high", "5.999999/6")
    
        self.assertEqual(uvRating(7.999999), "high", "7.999999/8")
        self.assertEqual(uvRating(8), "very high", "7.999999/8")
    
        self.assertEqual(uvRating(10.999999),"very high", "10.999999/11")
        self.assertEqual(uvRating(11),"extreme", "10.999999/11")

