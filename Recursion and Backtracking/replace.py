## Read input as specified in the question.
## Print output as specified in the question.
"""
Given an input string S and two characters c1 and c2,
you need to replace every occurrence of character c1 with character c2 in the given string.
"""

def replaceCharacter(string, c1, c2): 
    if len(string)==0: 
        return string 
    string2 = replaceCharacter(string[1:],c1,c2) 
    if string[0]==c1: 
        return c2 + string2 
    else: 
        return string[0] + string2


string = input().strip() 
c1, c2 = (i for i in input().strip().split(' '))
print(replaceCharacter(string, c1, c2))
