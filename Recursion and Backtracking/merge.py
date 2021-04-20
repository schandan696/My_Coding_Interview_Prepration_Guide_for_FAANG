def mergeArr(arr1, arr2):
    n1, n2 = len(arr1), len(arr2)
    i, j, k = 0, 0, 0
    arr3 = [0]*(n1+n2)
    while i < n1 and j < n2:
        if arr1[i] <= arr2[j]:
            arr3[k] = arr1[i]
            i += 1
        else:
            arr3[k] = arr2[j]
            j += 1
        k += 1
    while i < n1:
        arr3[k] = arr1[i]
        i += 1
        k += 1
    while j < n2:
        arr3[k] = arr2[j]
        j += 1
        k += 1
    return arr3

def merge(arr):
    if len(arr) <= 1:
        return arr
    m = int(len(arr)/2)
    left = merge(arr[:m])
    right = merge(arr[m:])
    return mergeArr(left, right)

arr1 = [3,4,1,6,8,9,4,11,5]
print(merge(arr1))