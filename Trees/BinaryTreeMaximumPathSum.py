# https://neetcode.io/problems/binary-tree-maximum-path-sum
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float('-inf')
        def dfs(root):
            if not root:
                return 0
            nonlocal maxSum
            lSum = dfs(root.left)
            rSum = dfs(root.right)
            greaterPath = max(lSum + root.val, rSum + root.val, root.val)
            maxSum = max(maxSum, greaterPath, greaterPath + min(lSum, rSum))
            return greaterPath
        dfs(root)
        return maxSum