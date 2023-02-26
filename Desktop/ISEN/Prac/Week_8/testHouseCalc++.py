from HouseCalcFixed import roomVolume

import unittest

TOL = 0.001

class HouseCalcTest(unittest.TestCase):

    def testroomVolume(self):
        self.assertEqual(abs(95.85 - roomVolume(3.0,7.1,4.5)) < TOL, roomVolume(3.0,7.1,4.5), "W >= 2, H >= 3, L >= 2.5")
    
        self.assertEqual(abs(0.0 - roomVolume(1.5,6.7,9.7)) < TOL,0.0,"W < 2, H >= 3, L >= 2.5")
    
        self.assertEqual (abs(0.0 - roomVolume(2.0,2.9,4.5)) < TOL,0.0, "W >= 2, H < 3, L >= 2.5")
    
        self.assertEqual (abs(0.0 - roomVolume(1.9,2.1,7.6)) < TOL,0.0, "W < 2, H < 3, L >= 2.5")
    
        self.assertEqual(abs(0.0 - roomVolume(4.0,5.5,2.0)) < TOL,0.0, "W >= 2, H >= 3, L <2.5")
    
        self.assertEqual(abs(0.0 - roomVolume(0.2,3.2,1.2)) < TOL,0.0, "W < 2, H >= 3, L < 2.5")
    
        self.assertEqual(abs(0.0 - roomVolume(8.2,2.6,0.7)) < TOL,0.0, "W >= 2, H >= 3, L < 2.5")
    
        self.assertEqual(abs(0.0 - roomVolume(1.3,1.7,1.8)) < TOL,0.0, "W <  2, H < 3, L < 2.5")


