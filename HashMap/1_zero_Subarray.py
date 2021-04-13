"""
You are given with an array (of size N) consisting of positive and negative integers that contain numbers in random order.
Write a program to return true if there exists a sub-array whose sum is zero else, return false.
Input Format :
  Line 1 : An Integer N i.e. size of array 
  Line 2 : N integers, elements of the array (separated by space)
Output Format :
  true or false
"""


def getValue(arr):
    s = set()
    _sum = 0
    for eachElement in arr:
        _sum += eachElement
        if _sum == 0 or _sum in s:
            return 'true'
        s.add(_sum)
    return 'false'

# Largest Continuous Sequence Zero Sum
def lszero(A):
        mp = {0:-1}
        s = 0
        start = end = 0
        
        for i in range(len(A)) :
            s += A[i]
            
            if s in mp :
                if i - mp[s] > end - start :
                    start = mp[s]
                    end = i 
            else :
                mp[s] = i
        
        return A[start+1:end+1]

arr = input().strip().split(" ")
n = int(arr[0])
arr = arr[1:n+1]
arr = [int(e) for e in arr]
print(getValue(arr))