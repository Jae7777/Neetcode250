# https://leetcode.com/problems/implement-queue-using-stacks/
class MyQueue:

    def __init__(self):
        self.stack = []
        self.r_stack = []

    def push(self, x: int) -> None:
        while self.r_stack:
            self.stack.append(self.r_stack.pop())
        self.stack.append(x)

    def pop(self) -> int:
        while self.stack:
            self.r_stack.append(self.stack.pop())
        return self.r_stack.pop()

    def peek(self) -> int:
        while self.stack:
            self.r_stack.append(self.stack.pop())
        return self.r_stack[-1]

    def empty(self) -> bool:
        return not self.stack and not self.r_stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()