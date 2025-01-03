# https://neetcode.io/problems/reorder-linked-list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s, f = head, head.next
        while f and f.next:
            f = f.next.next
            s = s.next
        c = s.next
        s.next = None
        p = None
        while c:
            n = c.next
            c.next = p
            p = c
            c = n
        l1, l2 = head, p
        while l2:
            t1, t2 = l1.next, l2.next
            l1.next = l2
            l2.next = t1
            l1, l2 = t1, t2
