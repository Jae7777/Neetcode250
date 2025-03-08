# https://neetcode.io/problems/kth-smallest-integer-in-bst
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = 0
        def getkth(root, currentK):
            nonlocal res
            if not root:
                return currentK
            l = getkth(root.left, currentK)
            if l + 1 == k:
                res = root.val
            r = getkth(root.right, l + 1)
            return r
        getkth(root, 0)
        return res