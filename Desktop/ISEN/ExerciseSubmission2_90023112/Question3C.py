def maxNumber():
    a = int(input("Enter 1st integer: "))
    b = int(input("Enter 2nd integer: "))
    c = int(input("Enter 3rd integer: "))
    d = int(input("Enter 4th integer: "))
# because the production code does not convert a,b,c,d to int so my test case is wrong. I change the production code as above
    if a >= b and a >= c and a >= d:
        result = a
    if b >= a and b >= c and b >= d:
        result = b
    if c >= a and c >= b and c >= d:
        result = c
    if d >= a and d >= b and d >= c:
        result = d

    print(result)

#maxNumber()
