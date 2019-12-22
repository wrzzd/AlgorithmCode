# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSS(self, root1, root2):
        if not root1 and not root2: return True
        if (root1 and not root2) or (not root1 and root2): return False
        if root1.val != root2.val: return False
        return self.isSS(root1.left, root2.right) and self.isSS(root1.right, root2.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        if not root.left and not root.right: return True
        if (not root.left and root.right) or (root.left and not root.right): return False
        l = root.left
        r = root.right
        return self.isSS(l, r)

