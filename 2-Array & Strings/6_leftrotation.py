def rotateLeft(d, arr):
    # return arr[d:] + arr[:d]
    temp = []
    n = len(arr)    
    d = d%n
    for i in range(d):
        temp.append(arr[i])
    print(temp)
    for i in range(n-d):
        arr[i] = arr[i+d]
    count = 0
    for i in range(n-d, n):
        arr[i] = temp[count]
        count+=1
    return arr
    