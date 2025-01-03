# https://neetcode.io/problems/merge-two-sorted-linked-lists
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ml = ListNode()
        mp1 = ml
        p1, l1 = None, list1
        p2, l2 = None, list2
        while l1 and l2:
            if l1.val < l2.val:
                mp1.next = ListNode(l1.val)
                l1 = l1.next
            else:
                mp1.next = ListNode(l2.val)
                l2 = l2.next
            mp1 = mp1.next
        mp1.next = l1 if l1 else l2 if l2 else None
        return ml.next
        
