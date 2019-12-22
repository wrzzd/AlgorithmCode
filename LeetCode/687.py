# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestRootUnivalue(self, root):
        if not root: return int(0)
        v = root.val
        res = 1
        if root.left and root.left.val == v:
            res += self.longestRootUnivalue(root.left)
        if root.right and root.right.val == v:
            res += self.longestRootUnivalue(root.right)
        return res - 1

    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root: return int(0)
        l, r = 0, 0
        if root.left:
            l = self.longestUnivaluePath(root.left)
        if root.right:
            r = self.longestUnivaluePath(root.right)
        return max(l, r, self.longestRootUnivalue(root))
