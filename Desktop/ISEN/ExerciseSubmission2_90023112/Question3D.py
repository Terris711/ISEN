import unittest
import sys, io
import Question3A 
import Question3B 
import Question3C

class TestSuite(unittest.TestCase):
    
    def test_printString(self):
        capOut = io.StringIO()
        sys.stdout = capOut
        Question3A.printString("coder","programmer")
        self.assertEqual("coder\n", capOut.getvalue(), "n is length of s1")

        capOut = io.StringIO()
        sys.stdout = capOut
        Question3A.printString("different","seafood")
        self.assertEqual("differe\n", capOut.getvalue(), "n is length of s2")

        capOut = io.StringIO()
        sys.stdout = capOut
        Question3A.printString("Xinchao","Xinchao")
        self.assertEqual("Xinchao\n", capOut.getvalue(), "n = length s1 = length s2")


        capOut = io.StringIO()
        sys.stdout = capOut
        Question3A.printString("","a")
        self.assertEqual("\n", capOut.getvalue(), "s1 has length smaller than n")

    def test_discount(self):
        
        self.assertEqual(0.0, Question3B.discount(-3,10), "Invalid age!")
        self.assertEqual(9.5, Question3B.discount(1,10), "5% discount")
        
        self.assertEqual(9.5, Question3B.discount(5,10), "5% discount!")
        self.assertEqual(8.5, Question3B.discount(6,10), "15% discount")
        
        self.assertEqual(8.5, Question3B.discount(16,10), "15% discount")
        self.assertEqual(10, Question3B.discount(17,10), "0% discount")
        
        self.assertEqual(10, Question3B.discount(35,10), "0% discount")
        self.assertEqual(7, Question3B.discount(36,10), "30% discount")

        self.assertEqual(7, Question3B.discount(49,10), "30% discount")
        self.assertEqual(5, Question3B.discount(50,10), "50% discount")
        
        self.assertEqual(5, Question3B.discount(80,10), "50% discount")

    def test_maxNumber(self):

        capOut = io.StringIO()
        sys.stdout = capOut
        sys.stdin = io.StringIO("9\n7\n8\n2")
        Question3C.maxNumber()
        self.assertEqual("Enter 1st integer: Enter 2nd integer: Enter 3rd integer: Enter 4th integer: 9\n", capOut.getvalue(), "a is largest number")

        capOut = io.StringIO()
        sys.stdout = capOut
        sys.stdin = io.StringIO("5\n8\n5\n6")
        Question3C.maxNumber()
        self.assertEqual("Enter 1st integer: Enter 2nd integer: Enter 3rd integer: Enter 4th integer: 8\n", capOut.getvalue(), "b is largest number")

        capOut = io.StringIO()
        sys.stdout = capOut
        sys.stdin = io.StringIO("7\n1\n21\n13")
        Question3C.maxNumber()
        self.assertEqual("Enter 1st integer: Enter 2nd integer: Enter 3rd integer: Enter 4th integer: 21\n", capOut.getvalue(), "c is largest number")

        capOut = io.StringIO()
        sys.stdout = capOut
        sys.stdin = io.StringIO("1\n2\n3\n4")
        Question3C.maxNumber()
        self.assertEqual("Enter 1st integer: Enter 2nd integer: Enter 3rd integer: Enter 4th integer: 4\n", capOut.getvalue(), "a is largest number")
