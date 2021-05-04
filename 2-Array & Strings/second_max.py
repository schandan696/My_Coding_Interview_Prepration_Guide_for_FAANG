import sys
def isNumber(s):
    """
    isNotNumber:
        Return True if Number else Flase
    """
    try:
        s = float(s)
        return True
    except:
        return False


def getRunnerUpNumber(arr):
    largest = str(-sys.maxsize) # Smallest Intiger
    second_largest = str(-sys.maxsize) # Smallest Intiger
    for eachChar in arr:
        # This condition check if array contain some invalid string that is not number 
        if not isNumber(eachChar):
            continue
        if int(largest) < int(eachChar):
            second_largest = largest
            largest = eachChar
        elif int(largest) > int(eachChar) and int(eachChar) > int(second_largest):
            second_largest = eachChar
    return second_largest if (second_largest != str(-sys.maxsize)) else -1

arr = ["3", "1", "8", "7", "2"]
# arr = ["3", "o", "-2"]
# arr = ["5", "5", "4", "2"]
# arr = ["4", "4", "4"] 
# arr = []
# arr = ["-214748364801","-214748364802"] 
print(getRunnerUpNumber(arr))