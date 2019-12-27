"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None
        stack = []
        stack.append(root)
        while stack:
            next_stack = []
            for i in range(len(stack)):
                if not stack[i].left:
                    next_stack.append(stack[i].left)
                    next_stack.append(stack[i].right)
                if i != len(stack) - 1:
                    stack[i].next = stack[i+1]
            stack = next_stack

        return root
