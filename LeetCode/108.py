# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums: return None
        if len(nums) == 1: return TreeNode(nums[0])
        if len(nums) == 2: 
            res = TreeNode(nums[1])
            res.left = TreeNode(nums[0])
        else:
            mid = int(len(nums) // 2)
            res = TreeNode(nums[mid])
            res.left = self.sortedArrayToBST(nums[0:mid])
            res.right = self.sortedArrayToBST(nums[mid+1:])
            return res
