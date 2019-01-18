'''
Created on 17 jan. 2019 at 14:12

@author: Olivier Gagnon

Question A
Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on the x-axis
and returns whether they overlap. As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).


Assumptions:
1) Only the version code is passed. No "v." or any variation of the word "version" and no software name.
2) Inputs are case sensitive and characters can be evaluated by their ascii value, meaning [A-Z] < [a-z] and [0-9] < [A-Za-z]
3) Any input to a version number raises its value shuch that 1.2 is smaller that 1.2.0 or 1.2.a
4) [.,\-_] are all considered as decimal notation if contiguous next to integers on both sides.
5) Sequences of 0' are only considered as part of a decimal number separated by a '.' ',' '-' or '_'.
6) Trailing or leading non alphanumerical symbols are dropped.
'''

import re

def greaterVersion(v1, v2):
    patternString = "[.,\-_]?[0-9]+|[.,\-_][0-9]+|[A-Z]|[a-z]"
    v1Elements = re.findall(patternString, v1)
    v2Elements = re.findall(patternString, v2)
    
    if v1 == v2:
        return "Same version"
    
    #get length of size of smallest list
    minLength = min(len(v1Elements), len(v2Elements))
     
    decimalSymbols = ["." , "," , "-" , "_"]
    
    for i in range(minLength):
        
        e1 = e2 = None
        
        #print(v1Elements[i] + "\t" + v2Elements[i])
        
        #Check if leading char of version 1 element is a decimal symbol or if it is a leading 0 at index 0.
        #If so replaces the first symbol by a dot and parse to float. 
        #Else, check if a number or letter through ascii value and parse or cast as int value accordingly.
        #Repeat for version 2 element.
        if v1Elements[i][0] in decimalSymbols or (i == 0 and v1Elements[i][0] == '0'):
            e1 = float(str("." + v1Elements[i][1:]))
        else:
            e1 = ord(v1Elements[i][0]) if ord(v1Elements[i][0]) >= 65 else int(v1Elements[i])
        
        if v2Elements[i][0] in decimalSymbols or (i == 0 and v2Elements[i][0] == '0'):
            e2 = float(str("." + v2Elements[i][1:]))
        else:
            e2 = ord(v2Elements[i][0]) if ord(v2Elements[i][0]) >= 65 else int(v2Elements[i])

        #return the greatest string if found.        
        if e1 > e2:
            return v1
        
        if e1 < e2:
            return v2
    
    #if reached the end without finding greatest value, return string with most elements 
    #(as added elements add value to version)
    if len(v1) > len(v2):
        return v1
    
    if len(v1) < len(v2):
        return v2
    
    #Covers the unplanned cases
    return "Undecided"
    

#Tests
print(greaterVersion("1.1", "1.1.1"))
print(greaterVersion("1.1", "1.0"))
print(greaterVersion("1", "1.0"))
print(greaterVersion("1.", "1.0"))
print(greaterVersion("A.1", "65.1"))
print(greaterVersion("1-a001a", "1.001"))
print(greaterVersion("1.01a", "1.001"))
print(greaterVersion("0001.a", "1.a"))
print(greaterVersion("10.45.00097", "10.44.99"))
print(greaterVersion("10.45.00097", "10.45.00098"))
print(greaterVersion("B10.45.00097", "Ba10.45.00098"))
print(greaterVersion("aB10.45.00097", "Ba10.45.00098"))
print(greaterVersion("AB10.45.00097", "Ba10.45.00097"))
print(greaterVersion("1-1,1.1", "1.1.1.1"))