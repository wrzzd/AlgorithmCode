# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []

        stack = [root]
        res = []
        while stack:
            now = stack.pop()
            res.append(now.val)
            if now.right:
                stack.append(now.right)
            if now.left:
                stack.append(now.left)
        return res
