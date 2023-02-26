# Python production code for ISE worksheet 6B.

def calcGrade(mark):
    """ 
    Calculates a grade, given a mark. For marks less than 50, the grade is 
    "F". For marks from 50 to 59, the grade is "5". For 60 to 69, the grade is 
    "6", and so on up to "10". If the mark is invalid, calcGrade will export 
    the empty string "".
    """
    
    grade = ""
    if isinstance(mark, int):
        if mark >= 0 and mark <= 100:
            if mark < 50:
                grade = "F"

            elif mark == 100:
                grade = "10"
        
            else:
                grade = str((mark + 1) // 10)
        
            return grade
        else:
            return "Mark is invalid"
    else:
        return "Mark have to be a number"


