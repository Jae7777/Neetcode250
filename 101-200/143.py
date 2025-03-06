# https://neetcode.io/problems/reorder-linked-list
# https://leetcode.com/problems/reorder-list/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find halfway point
        s, f = head, head.next
        while f and f.next:
            f = f.next.next
            s = s.next
        # reverse second half
        c = s.next
        s.next = None
        p = None
        while c:
            n = c.next
            c.next = p
            p = c
            c = n
        # merge two halves
        l1, l2 = head, p
        while l2:
            t1, t2 = l1.next, l2.next
            l1.next = l2
            l2.next = t1
            l1, l2 = t1, t2
