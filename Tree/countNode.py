class Node:
    def __init__(self ,key):
        self.data = key
        self.left = None
        self.right = None
  
def getfullCount(root):
    if root is None:
        return 0
    return 1 + getfullCount(root.left) + getfullCount(root.right)
  
# Driver Program to test above function
root = Node(2)
root.left = Node(7)
root.right = Node(5)
root.left.right = Node(6)
root.left.right.left = Node(1)
root.left.right.right = Node(11)
root.right.right = Node(9)
root.right.right.left = Node(4)
print(getfullCount(root))