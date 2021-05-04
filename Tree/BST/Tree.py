class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    
    def __init__(self):
        self.root = None
        self.numNodes = 0
    
    def __insert(self, root, data):
        if root is None:
            return BinaryTreeNode(data)
        if root.data >= data:
            root.left = self.__insert(root.left, data)
            return root
        else:
            root.right = self.__insert(root.right, data)
            return root
    
    def __printTree(self, root):
        if root is None:
            return
        print(root.data,end=":")
        if root.left:
            print("L:{}".format(root.left.data),end=",")
        if root.right:
            print("R:{}".format(root.right.data),end="")
        print()
        self.__printTree(root.left)
        self.__printTree(root.right)

    def __search(self, root, data):
        if root is None:
            return False
        if root.data == data:
            return True
        if root.data < data:
            return self.__search(root.right, data)
        else:
            return self.__search(root.left, data)

    def printTree(self):
        self.__printTree(self.root)
    
    
    def search(self, data):
        return self.__search(self.root, data)

        
    def insert(self, data):
        self.numNodes += 1
        self.root = self.__insert(self.root, data)
    def __max(self, root):
        if root is None:
            return None
        if root.right is None:
            return root.data
        return self.__max(root.right)

    def __delete(self, root, data):
        if root is None: 
            return None
        if root.data == data and root.left is None and root.right is None:
            return None
        elif root.data == data and root.left is None:
            return root.right
        elif root.data == data and root.right is None:
            return root.left
        elif root.data == data and root.right and root.left:
             maxE = self.__max(root.left)
             root.data = maxE
             root.left = self.__delete(root.left, maxE)
        if root.data > data:
            root.left = self.__delete(root.left, data)
            return root
        else:
            root.right = self.__delete(root.right, data)
            return root

    def delete(self, data):
        return self.__delete(self.root, data)
    
    def count(self):
        return self.numNodes
        
b = BST()
b.insert(5)
b.insert(4)
b.insert(6)
b.insert(1)
b.insert(2)
b.insert(3)
b.insert(7)
b.insert(8)
b.printTree()
# print(b.search(5))
print('---')
b.delete(5)
b.printTree()