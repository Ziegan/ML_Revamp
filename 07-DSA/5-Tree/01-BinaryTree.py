class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preOrderTraversal(node):
    if node is None:
        return
    print(node.data, end=", ")
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)


def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=", ")
    inOrderTraversal(node.right)


def postOrderTraversal(node):
    if node is None:
        return
    postOrderTraversal(node.left)
    postOrderTraversal(node.right)
    print(node.data, end=", ")


root = TreeNode("R")
nodeA = TreeNode("A")
nodeB = TreeNode("B")
nodeC = TreeNode("C")
nodeD = TreeNode("D")
nodeE = TreeNode("E")
nodeF = TreeNode("F")
nodeG = TreeNode("G")

root.left = nodeA  ##L1
root.right = nodeB  ##L1

nodeA.left = nodeC  ##L2
nodeA.right = nodeD  ##L2

nodeB.left = nodeE  ##L2
nodeB.right = nodeF  ##L2

nodeF.left = nodeG  ##L3

print("root.right.left.data:", root.right.left.data)

##Traversing
# preOrderTraversal(root)
inOrderTraversal(root)
# postOrderTraversal(root)
