# https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
from typing import Optional

class Solution:
    def gcd(self, n, m):
        if n % m == 0:
            return m
        return self.gcd(m, n % m)

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr.next:
            gcd = self.gcd(curr.val, curr.next.val)
            node = ListNode(gcd, curr.next)
            curr.next = node
            curr = curr.next.next
        return head