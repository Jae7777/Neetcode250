# https://leetcode.com/problems/design-circular-queue/
class Node:
    def __init__(self, val: int = 0, next = None):
        self.val = val
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.front = None
        self.rear = None
        self.k = k
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.size == self.k:
            return False
        node = Node(value)
        if not self.front and not self.rear:
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        if not self.front.next:
            self.front = self.rear = None
        else:
            front = self.front
            self.front = self.front.next
            del front
        self.size -= 1
        return True

    def Front(self) -> int:
        return self.front.val if self.front else -1
        
    def Rear(self) -> int:
        return self.rear.val if self.rear else -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()