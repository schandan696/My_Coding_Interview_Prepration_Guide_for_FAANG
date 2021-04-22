def subSeq(s, out):
    if len(s) == 0:
        print(out)
        return ['']
    output = subSeq(s[1:], out)
    output = subSeq(s[1:], out+s[0])

s = "abc"
subSeq(s, '')