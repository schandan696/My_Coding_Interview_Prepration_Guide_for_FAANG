"""
Return all prossible subsequuence
input: "abc"
Output: ['', 'c', 'b', 'bc', 'a', 'ac', 'ab', 'abc']
"""

def subSeq(s):
    if len(s) <=0:
        return ['']
    output = subSeq(s[1:])
    ans = []
    for eachOb in output:
        ans.append(s[0]+eachOb)
    return output + ans

s = "abc"
print(subSeq(s))