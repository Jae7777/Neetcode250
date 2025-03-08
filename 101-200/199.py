# https://neetcode.io/problems/binary-tree-right-side-view
# https://leetcode.com/problems/binary-tree-right-side-view/description/
from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque([root])
        while q:
            newQ = deque()
            foundRight = False
            while q:
                n = q.popleft()
                if n:
                    newQ.append(n.right)
                    newQ.append(n.left)
                    if not foundRight:
                        res.append(n.val)
                        foundRight = True
            q = newQ
        return res
