#!python3
"""
##### Problem 2
Create a function that determines if a triangle is scalene, right or obtuse.  
3 input parameters:  
float: one side  
float: another side  
float: 3rd side  

return:
0 : triangle does not exist
1 : if the triangle is acute
2 : if the triangle is right
3 : if the triangle is obtuse

Sample assertions:  
assert triangle(12,5,13) == 2     
assert triangle(5,3,3) == 3  
assert triangle(5,15,12) == 3  
assert triangle(1,1,4) == 0  
(2 points)
"""
import math

def triangle(a,b,c):
    hyp = max(a,b,c)

    #determining the hypoteneuse
    if hyp == c:
        side1 = a
        side2 = b
    
    elif hyp == b:
        side1 = a
        side2 = c

    elif hyp == a:
        side1 = c
        side2 = b

    #determining the type of triangle
    if side1 + side2 <hyp:
        return 0 

    if side1**2+side2**2>hyp**2:
        return 1

    if side1**2+side2**2==hyp**2:
        return 2

    if side1**2+side2**2<hyp**2:
        return 3
    



def tests():
    assert triangle(12,5,13) == 2     
    assert triangle(5,3,3) == 3  
    assert triangle(5,15,12) == 3  
    assert triangle(1,1,4) == 0  


if __name__== "__main__":
    tests()
