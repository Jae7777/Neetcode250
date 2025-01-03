# https://neetcode.io/problems/linked-list-cycle-detection
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        t, h = head, head.next
        while h and h.next:
            t = t.next
            h = h.next.next
            if t == h:
                return True
        return False