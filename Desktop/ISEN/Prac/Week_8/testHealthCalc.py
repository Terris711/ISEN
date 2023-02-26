from HealthCalc import uvRating

def testHealthCalc():
    print("Test 1")
    assert uvRating(-1) == "-", "index < 0" 
    
    assert uvRating(2) == "low", "0 <= index < 3" 
    
    assert uvRating(5) == "moderate", "3 <= index < 6" 
    
    assert uvRating(7) == "high", "6 <= index < 8" 
    
    assert uvRating(9) == "very high", "8 <= index < 11" 
    
    assert uvRating(13) == "extreme", "index > 11"

def testHealthCalcBVA():
    print("Test 2")
    assert uvRating(-0.0001) == "-", "Invalid/0"
    assert uvRating(2.999999) == "low", "2.999999/3"

    assert uvRating(2.999999) == "low", "2.999999/3"
    assert uvRating(3) == "moderate", "2.999999/3"
    
    assert uvRating(5.999999) == "moderate", "5.999999/6"
    assert uvRating(6) == "high", "5.999999/6"
    
    assert uvRating(7.999999) == "high", "7.999999/8"
    assert uvRating(8) == "very high", "7.999999/8"
    
    assert uvRating(10.999999) == "very high", "10.999999/11"
    assert uvRating(11) == "extreme", "10.999999/11"

print("Testing")
testHealthCalc()

testHealthCalcBVA()
