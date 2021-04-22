def keypad(num):
    options = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    if num == 0:
        return [""]
    val = num%10
    smallOut = keypad(num//10)
    ans = []
    for eachChar in options[val]:
        for eachO in smallOut:
            ans.append(eachO+eachChar)
    return ans

print(keypad(23))