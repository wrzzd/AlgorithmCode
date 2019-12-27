# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head: return None
        slow = head

        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if not slow.next:
            return TreeNode(slow.val)
        res = TreeNode(slow.next.val)
        half_end = slow.next.next
        slow.next = None
        res.left = self.sortedListToBST(head)
        res.right = self.sortedListToBST(half_end)
        return res
            
