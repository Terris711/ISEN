#
# testUtils.py
#

import unittest 
import sys, io
import Utils



class TestSuite(unittest.TestCase):
    def test_printCoordinates(self):
        capOut = io.StringIO()
        sys.stdout = capOut
        Utils.printCoordinates(4.7,3.141516784,8.986)
        self.assertEqual("(4.70,3.14,8.99)\n", capOut.getvalue(), "Printed coordinates")


    def test_readChar(self):
        validChar = "PHONE"
        sys.stdin = io.StringIO("P\nPH\nH\nA\nO")
        self.assertEqual("P", Utils.readChar(validChar), "Valid character!")
        self.assertEqual("H", Utils.readChar(validChar), "Longer than 1 character")
        self.assertEqual("O", Utils.readChar(validChar), "Invalid character")


    def test_guessingGame(self):
        guessNumber = 10

        capOut = io.StringIO()
        sys.stdout = capOut
        sys.stdin = io.StringIO("10")
        Utils.guessingGame(guessNumber)
        self.assertEqual("Enter an integer: Correct!\n", capOut.getvalue(), "Correct guess!")


        capOut = io.StringIO()
        sys.stdout = capOut
        sys.stdin = io.StringIO("11\n10")
        Utils.guessingGame(guessNumber)
        self.assertEqual("Enter an integer: Too high.\nEnter an integer: Correct!\n", capOut.getvalue(), "Correct guess!")


        capOut = io.StringIO()
        sys.stdout = capOut
        sys.stdin = io.StringIO("11\n9\n10")
        Utils.guessingGame(guessNumber)
        self.assertEqual("Enter an integer: Too high.\nEnter an integer: Too low.\nEnter an integer: Correct!\n", capOut.getvalue(), "Correct guess!")
    

    
    def test_sumFile(self):
        
        f =  open("testFile.txt","w", encoding='utf8')
        f.write("2.0\n5.0\n8.0")
        f.close()

        f2 = open("testFile2.txt","w", encoding='utf8') 
        f2.close()

        self.assertEqual(-1.0, Utils.sumFile("testFile1.txt"),"File does not exist!")
        self.assertEqual(0.0, Utils.sumFile("testFile2.txt"),"Empty file!")
        self.assertEqual(15.0, Utils.sumFile("testFile.txt"),"Sum is calculated!")


    def test_saveData(self):
        

        self.assertEqual(False, Utils.saveData("", "Anna", 8.5, 90), "Can not read file!")

        self.assertEqual(True, Utils.saveData("outfile.txt", "Anna", -1.0, 90), "Dead!")

        self.assertEqual(True, Utils.saveData("outfile.txt", "Anna", 8.5, 100), "Won!")

        self.assertEqual(True, Utils.saveData("outfile.txt", "Anna", 8.5, 90), "Won!")

        
        


