# https://leetcode.com/problems/house-robber-iii/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        def dfs(root):
            if not root:
                return 0
            if root in memo:
                return memo[root]
            currRoute = root.val
            if root.left:
                currRoute += dfs(root.left.left) + dfs(root.left.right)
            if root.right:
                currRoute += dfs(root.right.left) + dfs(root.right.right)
            skipRoute = dfs(root.left) + dfs(root.right)
            memo[root] = max(currRoute, skipRoute)
            return memo[root]
        return dfs(root)