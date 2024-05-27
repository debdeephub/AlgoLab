class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# class Solution:
#     def heightTree(self,root):
#         if root is None:
#             return 0
#         if root.left is None and root.right is None:
#             return 1
#         else:
#             return max(self.heightTree(root.left),self.heightTree(root.right))+1

class Solution:
    def heightTree(self,root):
        if root is None:
            return 0
        return max(self.heightTree(root.left),self.heightTree(root.right))+1
        
        
    

bt1 = BinaryTreeNode(1)
bt2 = BinaryTreeNode(2)
bt3 = BinaryTreeNode(3)
bt4 = BinaryTreeNode(4)
bt5 = BinaryTreeNode(5)

bt1.left = bt2
bt1.right = bt3

bt2.left = bt4
bt2.right = bt5

print(Solution().heightTree(bt1))