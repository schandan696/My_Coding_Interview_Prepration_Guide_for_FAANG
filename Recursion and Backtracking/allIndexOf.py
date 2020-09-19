def allIndex(arr, x, i):
    if i == len(arr):
        return ''
    if arr[i] == x:
        s = str(i) + ' '
    else:
        s = ''
    return s + allIndex(arr, x, i+1)

if __name__ == "__main__":
    arr = [9, 8, 10, 8, 8]
    x = 8
    print(allIndex(arr, x, 0))