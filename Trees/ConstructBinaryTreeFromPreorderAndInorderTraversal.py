# https://neetcode.io/problems/binary-tree-from-preorder-and-inorder-traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderindexes = {}
        for i, n in enumerate(inorder):
            inorderindexes[n] = i
        pindex = 0
        def constructTree(left, right):
            nonlocal pindex
            if left > right:
                return None
            n = preorder[pindex]
            m = inorderindexes[n]
            root = TreeNode(n)
            pindex += 1
            root.left = constructTree(left, m - 1)
            root.right = constructTree(m + 1, right)
            return root

        return constructTree(0, len(inorder) - 1)