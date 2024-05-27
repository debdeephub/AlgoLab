class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def printDetailedTree(self,root):
        if root is None:
            return
        # if root.left is not None and root.right is not None:
        #     print(root.data,end=":")
        print(root.data,end=":")
        if root.left is not None:
            print("L",root.left.data,end=",")
        if root.right is not None:
            print("R",root.right.data,end="")
        print()
        self.printDetailedTree(root.left)
        self.printDetailedTree(root.right)


bt1 = BinaryTreeNode(1)
bt2 = BinaryTreeNode(4)
bt3 = BinaryTreeNode(5)

bt1.left = bt2
bt1.right = bt3

Solution().printDetailedTree(bt1)