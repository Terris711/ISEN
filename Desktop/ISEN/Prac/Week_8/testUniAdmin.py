from UniAdminFixed import calcGrade

def testcalcGrade():
    print("Run 1")
    assert calcGrade(-9) == "Mark is invalid", "Mark < 0"

    assert calcGrade(32) == "F", "0 <= Mark < 50"
    
    assert calcGrade(55) == "5", "50 <= Mark < 60"
    
    assert calcGrade(63) == "6", "60 <= Mark < 70"
    
    assert calcGrade(72) == "7", "70 <= Mark < 80"
    
    assert calcGrade(88) == "8", "80 <= Mark < 90"
    
    assert calcGrade(91) == "9", "90 <= Mark < 100"
    
    assert calcGrade(100) == "10", "Mark = 100"
    
    assert calcGrade(102) == "Mark is invalid", "Mark > 100"

def testcalcGradeBVA():
    print("Run 2")
    assert calcGrade(-1) =="Mark is invalid", "Invalid/Fail"
    assert calcGrade(0) =="F", "Invalid/Fail"

    assert calcGrade(47) =="F", "Fail/5"
    assert calcGrade(50) =="5", "Fail/5"
    
    assert calcGrade(58) =="5", "5/6"
    assert calcGrade(60) =="6", "5/6"
    
    assert calcGrade(64) =="6", "6/7"
    assert calcGrade(70) =="7", "6/7"
    
    assert calcGrade(74) =="7", "7/8"
    assert calcGrade(80) =="8", "7/8"

    assert calcGrade(85) =="8", "8/9"
    assert calcGrade(90) =="9", "8/9"
    
    assert calcGrade(93) =="9", "9/10"
    assert calcGrade(100) =="10", "9/10"

    assert calcGrade(101) =="Mark is invalid", "10/Invalid"

print("Running Main")
testcalcGrade()
testcalcGradeBVA()
