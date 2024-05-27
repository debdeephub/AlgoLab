class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def numOfLeafNodes(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return numOfLeafNodes(root.left) + numOfLeafNodes(root.right)



bt1 = BinaryTreeNode(1)
bt2 = BinaryTreeNode(2)
bt3 = BinaryTreeNode(3)
bt4 = BinaryTreeNode(4)
bt5 = BinaryTreeNode(5)

bt1.left = bt2
bt1.right = bt3

bt2.left = bt4
bt2.right = bt5

print(numOfLeafNodes(bt1))
