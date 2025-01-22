# https://leetcode.com/problems/reverse-linked-list-ii/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverseList(before, start, end, after):
            prev = None
            curr = start
            stop = end.next
            while curr != stop:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            before.next = end
            start.next = after
        dummy = ListNode(next=head)
        i = 1
        ln = rn = None
        curr = head
        while i < right and curr:
            if i + 1 == left:
                ln = curr
            i += 1
            curr = curr.next
        rn = curr
        if ln == None:
            ln = dummy
        reverseList(ln, ln.next, rn, rn.next)
        return dummy.next