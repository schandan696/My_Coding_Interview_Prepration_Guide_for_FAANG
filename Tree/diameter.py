class Node: 
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
def maxDiameter(node):
    if node is None:
        return (0, 0)
    l_height, d1 = maxDiameter(node.left)
    r_height, d2 = maxDiameter(node.right)
    height = max(l_height, r_height) + 1
    return (height, max(l_height+r_height, d1, d2))

 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
print ("Height of tree is %d %d" %(maxDiameter(root)))
