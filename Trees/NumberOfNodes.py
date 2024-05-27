class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def numOfNodes(root):
    if root is None:
        return 0
    return 1 + numOfNodes(root.left) + numOfNodes(root.right)


bt1 = BinaryTreeNode(1)
bt2 = BinaryTreeNode(2)
bt3 = BinaryTreeNode(3)
bt4 = BinaryTreeNode(4)
bt5 = BinaryTreeNode(5)

bt1.left = bt2
bt1.right = bt3

bt2.left = bt4
bt2.right = bt5

print(numOfNodes(bt1))
