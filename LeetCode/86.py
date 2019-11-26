# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        l = None
        re = None
        
        while head:
            if head.val < x:
                if not l:
                    l = ListNode(head.val)
                    l_head = l
                else:
                    l.next = ListNode(head.val)
                l = l.next
            else:
                if not re:
                    re = ListNode(head.val)
                    re_head = re
                else:
                    re.next = ListNode(head.val)
                re = re.next
            head = head.next
        if not l_head:
            return re_head

        l.next = re_head
        return l_head
