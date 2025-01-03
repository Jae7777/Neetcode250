# https://neetcode.io/problems/serialize-and-deserialize-binary-tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    class DummyNode:
        def __init__(self, next=None):
            self.next = next
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        q = deque([root])
        while q:
            newQ = deque()
            while q:
                n = q.popleft()
                if n:
                    res.append(str(n.val))
                    newQ.append(n.left)
                    newQ.append(n.right)
                else:
                    res.append('null')
            q = newQ
        return ','.join(res)
    
    def createNode(self, s):
        if s == 'null':
            return None
        return TreeNode(int(s))
    
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        li = data.split(',')
        if len(li) == 0:
            return None
        res = self.createNode(li[0])
        q = deque([res])
        for i in range(1, len(li), 2):
            n1 = self.createNode(li[i])
            n2 = self.createNode(li[i+1]) if i < len(li) else None
            n = q.popleft()
            n.left = n1
            n.right = n2
            if n1:
                q.append(n1)
            if n2:
                q.append(n2)
        return res
