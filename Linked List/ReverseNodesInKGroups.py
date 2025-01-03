# https://neetcode.io/problems/reverse-nodes-in-k-group
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l, r = head, head
        res = ListNode(next=head)
        prevEnd = res
        while r:
            i = 1
            while i < k and r.next:
                r = r.next
                i += 1
            if i != k:
                break
            nextStart = r.next
            p, c = nextStart, l
            while c != nextStart:
                n = c.next
                c.next = p
                p = c
                c = n
            prevEnd.next = r
            prevEnd = l
            l = r = nextStart
        return res.next