class Node:
     
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTree(inOrder, preOrder):
    if len(preOrder) == 0 and len(inOrder) == 0:
        return None
    if len(preOrder) == 1 and len(inOrder) == 1:
        return Node(preOrder[0])
    rootData = preOrder[0]
    indexInOrder = inOrder.index(rootData)
    InOL = inOrder[0:indexInOrder]
    InOR = inOrder[(indexInOrder+1):]
    PreL = preOrder[1:len(InOL)+1]
    PreR = preOrder[len(InOL)+1:]
    root = Node(rootData)
    root.left = buildTree(PreL, InOL)
    root.right = buildTree(PreR, InOR)
    return root
 
def search(arr, start, end, value):
    for i in range(start, end + 1):
        if arr[i] == value:
            return i
 
def printInorder(node):
    if node is None:
        return
    printInorder(node.left)
    print(node.data, end=" ")
    printInorder(node.right)
     
inOrder = ['D', 'B', 'E', 'A', 'F', 'C']
preOrder = ['A', 'B', 'D', 'E', 'C', 'F']
buildTree.preIndex = 0
root = buildTree(inOrder, preOrder)
 
print("Inorder traversal of the constructed tree is")
printInorder(root)