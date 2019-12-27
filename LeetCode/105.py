# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder: return None
        res = TreeNode(preorder[0])
        root_index = inorder.index(preorder[0])

        res.left = self.buildTree(preorder[1: 1 + root_index], inorder[0:root_index])
        res.right = self.buildTree(preorder[1+root_index:], inorder[root_index+1:])

        return res
