# https://neetcode.io/problems/linked-list-cycle-detection
# https://leetcode.com/problems/linked-list-cycle/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        t, h = head, head.next
        while h and h.next:
            t = t.next
            h = h.next.next
            if t == h:
                return True
        return False