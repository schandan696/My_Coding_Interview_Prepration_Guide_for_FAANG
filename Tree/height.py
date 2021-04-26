class Node: 
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
def maxHeight(node):
    if node is None:
        return 0
    l = maxHeight(node.left)
    r = maxHeight(node.right)
    return max(l, r) + 1

 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print ("Height of tree is %d" %(maxHeight(root)))
