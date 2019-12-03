# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return None
        now_layer = [root]
        res = []
        while len(now_layer) > 0:
            layer_res = []
            next_layer = []
            for node in now_layer:
                layer_res.append(node.val)
                if node.left: next_layer.append(node.left)
                if node.right: next_layer.append(node.right)
            res = [layer_res] + res
            now_layer = next_layer
        return res
