# A function reads marks of a student for different units form a file/record store them in an array
# Assume I already had marks.csv (is the file contains student's marks)
def readMarks():
    fileobj = open('marks.csv', 'r')
    data = fileobj.readlines()
    while data:
        mark = data.strip().split(',')
        marks.append(mark)
    fileobj.close()
    return marks

# A function counts the values of an array which are less than 50 and store the count in a variable
def counts(marks):
    count = 0
    for i in range (len(marks)):
        if marks[i] < 50:
            count += 1
    return count
# A function prints the prints an array's element
def prints(marks):
    print("List of marks: ")
    for i in range (len(marks)):
        print(marks[i])

if __name__ == "__main__":

# Global variables
    marks = []
    studentMarks = readMarks()
    countMarks = counts(studentMarks)
    # print a count variable - I don't want to put it in prints function because it will duplicate the code!
    print("Marks less than 50 is: ", countMarks)
    prints(studentMarks)
    

    
