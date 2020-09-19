def firstIndex(arr, x, i):
    if i == len(arr):
        return -1
    if arr[i] == x:
        return i
    return firstIndex(arr, x, i+1)

if __name__ == "__main__":
    arr = [9, 8, 10, 8]
    x = 8
    print(firstIndex(arr, x, 0))
