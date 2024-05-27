class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printNodesAtK(root,k):
    if root is None:
        return
    if k == 0:
        print(root.data)
        return
    printNodesAtK(root.left,k-1)
    printNodesAtK(root.right,k-1)

def printNodesAtKv2(root,k,d=0):
    if root is None:
        return
    if k == d:
        print(root.data)
        return
    printNodesAtKv2(root.left,k,d+1)
    printNodesAtKv2(root.right,k,d+1)



bt1 = BinaryTreeNode(1)
bt2 = BinaryTreeNode(2)
bt3 = BinaryTreeNode(3)
bt4 = BinaryTreeNode(4)
bt5 = BinaryTreeNode(5)

bt1.left = bt2
bt1.right = bt3

bt2.left = bt4
bt2.right = bt5


# printNodesAtK(bt1, 2)
printNodesAtKv2(bt1, 2)