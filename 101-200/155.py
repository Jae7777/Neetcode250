# https://neetcode.io/problems/minimum-stack
# https://leetcode.com/problems/min-stack/description/

class MinStack:

    def __init__(self):
        self.minStack = []

    def push(self, val: int) -> None:
        if self.minStack:
            self.minStack.append((val, min(val, self.minStack[-1][1])))
        else:
            self.minStack.append((val, val))

    def pop(self) -> None:
        self.minStack.pop()

    def top(self) -> int:
        return self.minStack[-1][0]

    def getMin(self) -> int:
        return self.minStack[-1][1]
