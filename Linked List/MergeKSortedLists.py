# https://neetcode.io/problems/merge-k-sorted-linked-lists
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self.mergeSort(lists, 0, len(lists) - 1)

    def mergeSort(self, lists, l, r) -> Optional[ListNode]:
        if l > r:
            return None
        if l == r:
            return lists[l]
        m = (l + r) // 2
        leftPartition = self.mergeSort(lists, l, m)
        rightPartition = self.mergeSort(lists, m + 1, r)
        return self.merge(leftPartition, rightPartition)

    def merge(self, l1, l2) -> Optional[ListNode]:
        res = c = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                c.next = l1
                l1 = l1.next
            else:
                c.next = l2
                l2 = l2.next
            c = c.next
        c.next = l1 or l2
        return res.next

