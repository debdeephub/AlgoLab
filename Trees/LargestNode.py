class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    def largestNode(self,root):
        if root == None:
            return -1
        leftLargest = self.largestNode(root.left)
        rightLargest = self.largestNode(root.right)
        largest = max(leftLargest,rightLargest,root.data)
        return largest
    

bt1 = BinaryTreeNode(1)
bt2 = BinaryTreeNode(2)
bt3 = BinaryTreeNode(3)
bt4 = BinaryTreeNode(4)
bt5 = BinaryTreeNode(5)

bt1.left = bt2
bt1.right = bt3

bt2.left = bt4
bt2.right = bt5

print(Solution().largestNode(bt1))