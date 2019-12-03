# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: return False
        if root.left: 
            root.left.val += root.val
            if self.hasPathSum(root.left, sum):
                return True
        if root.right: 
            root.right.val += root.val
            if self.hasPathSum(root.right, sum):
                return True
        if not root.left and not root.right:
            if root.val == sum:
                return True
        return False
            
