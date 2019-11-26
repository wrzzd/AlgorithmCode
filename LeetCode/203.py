# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head: return head
        res = None
        while head and head.val == val:
            head = head.next
        if not head: return res
        res = head
        while True:
            if not head or not head.next:
                break
            if head.next.val == val:
                if head.next.next:
                    head.next = head.next.next
                    
                else:
                    head.next = None
            else:
                head = head.next
            
        return res
