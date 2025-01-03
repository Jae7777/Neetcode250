# https://neetcode.io/problems/level-order-traversal-of-binary-tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        res = []
        while q:
            newQ = deque()
            newLi = []
            while q:
                n = q.popleft()
                if n:
                    newLi.append(n.val)
                    newQ.append(n.left)
                    newQ.append(n.right)
            if newLi:
                res.append(newLi)
            q = newQ
        return res
