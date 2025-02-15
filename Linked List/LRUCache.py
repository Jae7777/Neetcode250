# https://neetcode.io/problems/lru-cache
class Node:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.count = 1
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def append(self, node):
        last = self.tail.prev
        node.prev = last
        node.next = self.tail
        last.next = node
        self.tail.prev = node
    
    def popleft(self):
        first = self.head.next
        self.head.next = first.next
        first.next.prev = self.head
        return first

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def empty(self):
        return self.head.next == self.tail

class LFUCache:

    def __init__(self, capacity: int):
        self.key_to_node = {}
        self.count_to_list = defaultdict(LinkedList)
        self.low = 0
        self.cap = capacity
        self.size = 0

    def use(self, node) -> None:
        self.count_to_list[node.count].remove(node)
        node.count += 1
        self.count_to_list[node.count].append(node)
        if self.count_to_list[self.low].empty():
            self.low = node.count

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        node = self.key_to_node[key]
        self.use(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.val = value
            self.use(node)
        else:
            if self.size == self.cap:
                node = self.count_to_list[self.low].popleft()
                del self.key_to_node[node.key]
                self.size -= 1
            node = Node(key, value)
            self.key_to_node[key] = node
            self.count_to_list[1].append(node)
            self.size += 1
            self.low = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)