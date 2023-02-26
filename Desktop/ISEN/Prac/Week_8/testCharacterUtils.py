from CharacterUtilsFixed import *

def testcharCase():
    assert charCase(True, "A"), "Checkupper is True and Ch is uppercase"

    assert not charCase(True, "a"), "Checkupper is true and Ch is lowercase"

def testsubstr():
    assert substr("paragraph","para") == "para" , "string 1 contain string 2"
    
    assert substr("beautiful","ugly") == "beautiful", "string 1 does not contain string 2"

    assert substr("phone", "phone") == "phone", "string 2 contains string 1"

    assert substr("coscience","science") == "science", "string 1 contains string 2"

testcharCase()
testsubstr()
