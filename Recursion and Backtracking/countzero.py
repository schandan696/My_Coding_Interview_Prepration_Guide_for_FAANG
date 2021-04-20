def countZeros(n):
    if n<0:
        n *= -1; # Make n positive
    if n<10:
        if n == 0:
            return 1
        return 0
    smallAns = countZeros(n // 10)
    if n%10==0:
        smallAns += 1
    return smallAns


arr= int(input())
print(countZeros(arr))