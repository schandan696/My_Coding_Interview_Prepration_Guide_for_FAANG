def getString(digit) :
    if digit == 2 :
        return 'abc'
    elif digit == 3 :
        return 'def'
    elif digit == 4 :
        return 'ghi'
    elif digit == 5 :
        return 'jkl'
    elif digit == 6 :
        return 'mno'
    elif digit == 7 :
        return 'pqrs'
    elif digit == 8 :
        return 'tuv'
    elif digit == 9 :
        return 'wxyz'
    else :
        return ''

def printKeypadHelper(n, output) :
    if n == 0 :
        print(output)
        return
    string = getString(n%10)
    for char in string :
        printKeypadHelper(n//10, char+output)

def printKeypad(n) :
    printKeypadHelper(n, '')

n = int(input().strip())
printKeypad(n)