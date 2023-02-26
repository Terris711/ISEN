def printString(s1, s2):
    if len(s1) < len(s2):
        n = len(s1)
        print(s1[:n])
    elif len(s2) < len(s1):
        n = len(s2)
        print(s1[:n])
    elif len(s1) == len(s2):
        n = len(s1)
        print(s1[:n])
    else:
        n = len(s1)
        print("") 


#s1 = input("Enter string s1: ")
#s2 = input("Enter string s2: ")
#print(printString(s1,s2))

