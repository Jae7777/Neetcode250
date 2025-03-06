# https://neetcode.io/problems/copy-linked-list-with-random-pointer
# https://leetcode.com/problems/copy-list-with-random-pointer/description/
"""
# Definition for a Node.
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

from typing import Optional
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes = {}
        h = head
        while h:
            nodes[h] = Node(h.val)
            h = h.next
        h = head
        while h:
            nodes[h].next = nodes[h.next] if h.next else None
            nodes[h].random = nodes[h.random] if h.random else None
            h = h.next
        return nodes[head] if head else None