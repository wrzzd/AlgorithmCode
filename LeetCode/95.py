# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0: return []
        if n == 1: return [TreeNode(1)]
        def generate(left, right):
            ans = []
            if left > right:
                return [None]
            for i in range(left, right + 1):
                left_ans = generate(left, i - 1)
                right_ans = generate(i + 1, right)
                for l in left_ans:
                    for r in right_ans:
                        t = TreeNode(i)
                        t.left = l
                        t.right = r
                        ans.append(t)
            return ans
        return generate(1, n)    
        # res = []
        # for t in self.generateTrees(n-1):
        #     add_tree = TreeNode(n)
        #     add_tree.left = t
        #     res.append(add_tree)
        #     adjoint = t
        #     while True:
        #         adjoint_now = adjoint
        #         if not adjoint_now.right:
        #             adjoint_now.right = TreeNode(n)
        #             res.append(adjoint_now)
        #             break
        #         else:
        #             a = TreeNode(n)
        #             a.left = adjoint_now.right
        #             adjoint_now.right = a
        #             res.append(adjoint_now)
