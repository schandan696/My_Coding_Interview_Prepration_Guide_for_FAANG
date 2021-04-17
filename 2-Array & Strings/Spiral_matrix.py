def spiralMatrix(m):
    left = 0
    right = 4
    top = 0
    bottom = 5

    while left <= right and top <= bottom:
        for i in range(left, right):
            print(m[top][i])
        top += 1 # 1
        for i in range(top,bottom):
            print(m[i][right-1])
        right -= 1 # 3
        for i in range(right-1, left-1, -1):
            print(m[bottom-1][i])
        bottom -= 1 #3
        for i in range(bottom-1, top-1, -1):
            print(m[i][left])
        left += 1

m = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
    [17, 18, 19, 20]
]
spiralMatrix(m)