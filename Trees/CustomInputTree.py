class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def treeInput():
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTreeNode(rootData)
    leftTree = treeInput()
    rightTree = treeInput()
    root.left = leftTree
    root.right = rightTree
    return root

def printTree(root):
    if root == None:
        return
    print(root.data, end = " ")
    printTree(root.left)
    printTree(root.right)

root = treeInput()
printTree(root)