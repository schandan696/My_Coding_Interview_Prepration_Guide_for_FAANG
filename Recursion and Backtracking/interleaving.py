"""
Given two strings S (of length m) and T (of length n), you need to find 
and print out all the possible inter leavings that are possible of length (m + n).
Inter leaving means - all possible combination of characters from both strings such 
that it contain all characters from both strings and, the respective ordering of characters 
of one string should remain same as in original.
"""

def Interleavings(s1, s2, s3):
    if len(s1) <= 0 and len(s2) <= 0:
        print(s3)
        return
    if len(s1) > 0:
        Interleavings(s1[1:], s2, s3+s1[0])
    if len(s2) > 0:
        Interleavings(s1, s2[1:], s3+s2[0])

s1 = input()
s2 = input()
Interleavings(s1, s2, "")