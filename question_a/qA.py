'''
Created on 17 jan. 2019 at 14:12

@author: Olivier Gagnon

Question A
Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on the x-axis
and returns whether they overlap. As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).


Assumptions:
1) A fucntion is sufficient, a command line input is not required (superficial).
2) Numbers can have decimals and be negative.
3) Inputs must be passed in the exact given form of (%d,%d)\n(%d,%d) without any spaces or letters.
4) Numbers must be ordered in each pair so that x1 <= x2 and x3 <= x4.

'''

import re


#Returns boolean, true if x2 > x3, false if not.
def hasOverlap(s):
    
    #Pattern of valid string, return "Invalid input string" if not match.
    pattern = re.compile("^[(]-?[0-9]+[.]?[0-9]*,-?[0-9]+[.]?[0-9]*[)]\n[(]-?[0-9]+[.]?[0-9]*,-?[0-9]+[.]?[0-9]*[)]$")
    
    if not pattern.match(s):
        return "Invalid input string"
    
    #Create a list from the numbers in s. 
    #could use regex groups to merge with validation, but messy.
    Xs = [float(numStr) for numStr in re.findall("-?[0-9]+[.]?[0-9]*", s)]
      
    #Check if number pairs are well ordered. 
    if Xs[0] > Xs[1] or Xs[2] > Xs[3]:
        return "Invalid numbers"
    
    return Xs[1] > Xs[2]

        
#Tests
print(hasOverlap("(-90,-60)\n(-60,7)")) #false
print(hasOverlap("(-90,-60)\n(-65,7)")) #true
print(hasOverlap("(1,76)\n(500,7)")) #false
print(hasOverlap("(1,76.75)\n(76.21,100)")) #true