# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head and head.next:
            f = head.next.next
            s = head.next
        else:
            return None
        
        while f:
            if f != s:
                if f.next:
                    f = f.next.next
                else:
                    return None

                s = s.next
            else:
                detection = head
                while detection != s:
                    s = s.next
                    detection = detection.next
                return detection
