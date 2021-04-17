class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
globalSum = 0
def printSum(root, nodeSum):
    global globalSum
    if root is None:
        print(nodeSum)
        globalSum += nodeSum
        return
    if root.left is None and root.right is None:
        print(nodeSum+root.data)
        globalSum += nodeSum+root.data
        return
    printSum(root.left, nodeSum+root.data)
    printSum(root.right, nodeSum+root.data)

        
root = Node(6)
root.left = Node(3)
root.right = Node(5)
root.left.left = Node(2)
root.left.right = Node(5)
root.left.right.left = Node(7)
root.left.right.right = Node(4)
root.right.right = Node(4)
printSum(root, 0)
print("global sum")
print(globalSum)