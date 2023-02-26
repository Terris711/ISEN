def avoidModule():

    fileobj = open('marks.csv', 'r')
    data = fileobj.readlines()
    while data:
        mark = data.strip().split(',')
    fileobj.close()

    if len(mark) > 0:
        count = 0
        i = 0
        while i < len(mark):
            studentMarks = int(mark[i])
            if studentMarks < 50:
                count += 1
            i += 1
        print("Student's marks: ")
        for i in range (len(mark)):
            print(mark[i])
        print("Marks < 50: ", count)
    else:
        print("Marks file is empty!")

if __name__ == "__main__":
    avoidModule()