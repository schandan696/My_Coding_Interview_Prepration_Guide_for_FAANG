from collections import OrderedDict
class newNode:
 
    # Construct to create a newNode
    def __init__(self, key):
        self.info = key
        self.left = None
        self.right = None
        self.hd = 0

ob = OrderedDict()
def topview(root, k, d):
    global ob
    if root is None:
        return
    if k not in ob:
        ob[k] = [root.info, d]
    elif ob[k][1] > d:
        ob[k] = [root.info, d]
    topview(root.left, k-1, d+1)
    topview(root.right, k+1, d+1)
    
def topView(root):
    topview(root, 0, 0)
    for i in sorted(ob.items()):
        print(i[1][0], end=" ")
    print()



if __name__ == '__main__':
 
    """ Create following Binary Tree
            1
        / \
        2 3
        \
            4
            \
            5
            \
                6*"""
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    root.right.left = newNode(6)
    root.right.right = newNode(7)
    print("Following are nodes in top",
          "view of Binary Tree")
    topView(root)