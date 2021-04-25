def printMatrix(sol):
    for eachLine in sol:
        print(eachLine)
    print("-----------------")

def hasPathHelper(maze, sol, x, y, n):
    if x == n-1 and y == n-1:
        sol[x][y] = 1
        printMatrix(sol)
        return True
    if (x < 0 or y < 0 or x>=n or y >= n or maze[x][y]==0 or sol[x][y]==1):
        return False
    sol[x][y] = 1
    a= hasPathHelper(maze, sol, x+1, y, n)
        # return True
    b = hasPathHelper(maze, sol, x, y+1, n)
        # return True
    c = hasPathHelper(maze, sol, x-1, y, n)
        # return True
    d = hasPathHelper(maze, sol, x, y-1, n)
        # return True
    sol[x][y] = 0
    return a or b or c or d

def hasPath(maze):
    sol = [[0 for j in range(4)] for i in range(4)]
    print(hasPathHelper(maze, sol, 0, 0, 4))
    



maze = [
    [1, 1, 1, 0],
    [1, 0, 1, 0],
    [1, 0, 1, 0],
    [0, 1, 1, 1]
]
hasPath(maze)