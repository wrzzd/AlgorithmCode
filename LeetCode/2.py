# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 : return l2
        if not l2 : return l1
        f = l1.val + l2.val
        if f < 10:
            res = ListNode(f)
            res.next = self.addTwoNumbers(l1.next, l2.next)
            return res
        else:
            res = ListNode(f % 10)
            res.next = self.addTwoNumbers(self.addTwoNumbers(l1.next, ListNode(1)), l2.next)
            return res
