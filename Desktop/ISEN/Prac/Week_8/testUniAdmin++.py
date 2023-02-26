from UniAdmin import calcGrade
import unittest

class UniAdminTest(unittest.TestCase):

    def testcalcGrade(self):
        print("Run 1")
        self.assertEqual(calcGrade(-9), "", "Mark < 0")

        self.assertEqual(calcGrade(32),"F", "0 <= Mark < 50")
    
        self.assertEqual(calcGrade(55),"5", "50 <= Mark < 60")
    
        self.assertEqual(calcGrade(63),"6", "60 <= Mark < 70")
    
        self.assertEqual(calcGrade(72),"7", "70 <= Mark < 80")
    
        self.assertEqual(calcGrade(88),"8", "80 <= Mark < 90")
    
        self.assertEqual(calcGrade(91),"9", "90 <= Mark < 100")
    
        self.assertEqual(calcGrade(100),"10", "Mark = 100")
    
        self.assertEqual(calcGrade(102),"", "Mark > 70")

    def testcalcGradeBVA(self):
        print("Run 2")
        self.assertEqual(calcGrade(-1),"", "Invalid/Fail")
        self.assertEqual(calcGrade(0),"F", "Invalid/Fail")

        self.assertEqual(calcGrade(49),"F", "Fail/5")
        self.assertEqual(calcGrade(50),"5", "Fail/5")
    
        self.assertEqual(calcGrade(59),"5", "5/6")
        self.assertEqual(calcGrade(60),"6", "5/6")
    
        self.assertEqual(calcGrade(69),"6", "6/7")
        self.assertEqual(calcGrade(70),"7", "6/7")
    
        self.assertEqual(calcGrade(79),"7", "7/8")
        self.assertEqual(calcGrade(80),"8", "7/8")

        self.assertEqual(calcGrade(89),"8", "8/9")
        self.assertEqual(calcGrade(90),"9", "8/9")
    
        self.assertEqual(calcGrade(99),"9", "9/10")
        self.assertEqual(calcGrade(100),"10", "9/10")

        selfassertEqual(calcGrade(101),"", "10/Invalid")

