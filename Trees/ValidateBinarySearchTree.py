# https://neetcode.io/problems/valid-binary-search-tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, lower, upper):
            if not root:
                return True
            if not (lower < root.val and root.val < upper):
                return False
            return dfs(root.left, lower, root.val) and dfs(root.right, root.val, upper)
        return dfs(root, float('-inf'), float('inf'))
