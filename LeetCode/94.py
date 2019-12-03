# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # if not root: return []
        # return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        res = []
        current = root
        if not root: return res
        while root:
            if not root.left:
                res.append(root.val)
                root = root.right
            else:
                left = root.left
                while left.right:
                    left = left.right
                left.right = root
                left.right.left = None
                root = root.left
            

        return res
