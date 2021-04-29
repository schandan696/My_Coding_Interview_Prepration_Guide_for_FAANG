INT_MIN = -2**32
 
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None 

def maxPathSum(root, res):
    if root is None:
        return 0
    l = maxPathSum(root.left, res)
    r = maxPathSum(root.right, res)
    if root.left is not None and root.right is not None:
        res[0] = max(res[0], l+r+root.data)
    return max(l,r)+root.data
 
 
# Driver program to test above function
root = Node(-15)
root.left = Node(5)
root.right = Node(6)
root.left.left = Node(-8)
root.left.right = Node(1)
root.left.left.left = Node(2)
root.left.left.right = Node(6)
root.right.left = Node(3)
root.right.right = Node(9)
root.right.right.right = Node(0)
root.right.right.right.left = Node(4)
root.right.right.right.right = Node(-1)
root.right.right.right.right.left = Node(10)
res = [0]
maxPathSum(root, res)
print("Max pathSum of the given binary tree is", res[0])