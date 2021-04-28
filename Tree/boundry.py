class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
import queue

def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length<=0 or levelorder[0]==-1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root

def PrintBoundaryLeft(root):
    if root is None:
        return
    if root.left is None and root.right is None:
        return
    if root.left:
    	print(root.data, end=" ")
    	PrintBoundaryLeft(root.left)
    else:
        print(root.data, end=" ")
        PrintBoundaryLeft(root.right)

def PrintBoundaryRight(root): 
    if root is None:
        return
    if root.left is None and root.right is None:
        return
    if root.right:
        print(root.data, end=" ")
        PrintBoundaryRight(root.right)
    else:
        print(root.data, end=" ")
        PrintBoundaryRight(root.left)
    

def PrintLeaves(root):
    if root is None:
        return
    if root.left is None and root.right is None:
        print(root.data, end=" ")
        return
    PrintLeaves(root.left)
    PrintLeaves(root.right)


def PrintBoundary(root):
    if(root!=None):
        print(root.data,end=" ")
    PrintBoundaryLeft(root.left)
    PrintLeaves(root.left)
    PrintLeaves(root.right)
    PrintBoundaryRight(root.right)

def solve(root):
    PrintBoundary(root)
    print()

levelOrder = [int(i) for i in input().strip().split()]
# print("1 2 3 -1 -1 -1 -1")
root = buildLevelTree(levelOrder)
solve(root)
