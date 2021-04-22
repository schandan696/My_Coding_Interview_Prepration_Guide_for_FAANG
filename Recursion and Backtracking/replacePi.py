'''
Given a string, compute recursively a new string where all appearances of "pi" have been replaced by "3.14".
Sample Input 1 : xpix
Sample Output : x3.14x
'''
def replacePi(s):
    if len(s) <= 1:
        return s
    if s[0:2] == "pi":
        return "3.14" + replacePi(s[2:])
    else:
        return s[0] + replacePi(s[1:])
    
s = input()
print(replacePi(s))






