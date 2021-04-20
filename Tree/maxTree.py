class Node:
      
    def __init__(self, key):
        self.key = key
        self.child = []
  
def maxSumUtil(root, maxsum):
    if root is None:
        return None
    currSum = root.key
    for eachNode in root.child:
        currSum += eachNode.key
        maxsum = maxSumUtil(eachNode, maxsum)
    maxsum = max(currSum, maxsum)
    return maxsum
def maxSum(root): 
  
    # resultant node with max 
    # sum of children and node
    resNode, maxsum = Node(None), 0
    maxsum = maxSumUtil(root, maxsum) 
    return maxsum
  
# Driver Code
if __name__ == "__main__":
  
    root = Node(1) 
    (root.child).append(Node(2)) 
    (root.child).append(Node(3)) 
    (root.child).append(Node(4)) 
    (root.child[0].child).append(Node(5)) 
    (root.child[0].child).append(Node(6)) 
    (root.child[2].child).append(Node(7)) 
    (root.child[2].child).append(Node(8)) 
    (root.child[2].child).append(Node(9)) 
    (root.child[2].child).append(Node(10)) 
  
    print(maxSum(root)) 
  
# This code is contributed by Rituraj Jain