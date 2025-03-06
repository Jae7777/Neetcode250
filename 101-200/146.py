# https://neetcode.io/problems/lru-cache
# https://leetcode.com/problems/lru-cache/
class Node:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next, self.tail.prev = self.tail, self.head

    def remove(self, node: Node) -> None:
        p, n = node.prev, node.next
        p.next, n.prev = n, p
    
    def insert(self, node: Node) -> None:
        self.tail.prev.next = node
        node.prev = self.tail.prev
        self.tail.prev = node
        node.next = self.tail

    def get(self, key: int) -> int:
        if key not in self.cache: 
            return -1
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            n = self.cache[key]
            n.val = value
            self.remove(n)
            self.insert(n)
        else:
            n = Node(key, value)
            self.cache[key] = n
            self.insert(n)
        if len(self.cache) > self.capacity:
            n = self.head.next
            self.remove(n)
            del self.cache[n.key]

            
