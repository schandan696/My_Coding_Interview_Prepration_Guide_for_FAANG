'''
Program for quick sort
'''

def piviot(a, start, end):
    piviot = end-1
    e = piviot-1
    i = start
    while i <= e:
        if a[i] > a[piviot]:
            a[i], a[e] = a[e], a[i]
            e -= 1
        else:
            i += 1
    a[piviot], a[i] = a[i], a[piviot]
    return i

def quickSort(a, start, end):
    if start >= end:
        return
    p = piviot(a, start, end)
    quickSort(a, start, p-1)
    quickSort(a, p+1, end)



arr = [3, 1, 11, 7, 6, 4, 12 , 2, 5]
quickSort(arr, 0, 9)
print(arr)