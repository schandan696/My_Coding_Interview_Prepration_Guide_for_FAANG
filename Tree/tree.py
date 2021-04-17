class TreeNode:
    def __init__(self, data):
        self.data = data
        self.child = []

class Tree:
    def __init__(self):
        self.head = None
    
    def __takeInput(self):
        print("Enter Data")
        rootData = input()
        rootNode = TreeNode(rootData)
        print("Enter the no of child")
        n = int(input())

        for i in range(n):
            child = self.__takeInput()
            rootNode.child.append(child)

        return rootNode

    def takeInput(self):
        self.head = self.__takeInput()

    def __print(self, node):
        print(node.data, end=" child:")
        for eachNode in node.child:
            print(eachNode.data, end=" ")
        print()
        for eachNode in node.child:
            self.__print(eachNode)
    
    def print(self):
        self.__print(self.head)

ob = Tree()
# rootNode = TreeNode(1)
# rootNode.child.append(TreeNode(2))
# rootNode.child.append(TreeNode(3))
# ob.head = rootNode
ob.takeInput()
# print(ob.head.data, ob.head.child)
ob.print()


