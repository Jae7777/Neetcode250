# https://leetcode.com/problems/insert-into-a-binary-search-tree/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from typing import Optional

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def insert(root):
            if not root:
                return TreeNode(val)
            if root.val < val:
                root.right = insert(root.right)
            else:
                root.left = insert(root.left)
            return root
        return insert(root)
