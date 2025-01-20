# https://leetcode.com/problems/maximum-frequency-stack/
class FreqStack:

    def __init__(self):
        self.count_val = defaultdict(list)
        self.val_count = defaultdict(int)
        self.top = 0

    def push(self, val: int) -> None:
        self.val_count[val] += 1
        self.count_val[self.val_count[val]].append(val)
        self.top = max(self.top, self.val_count[val])

    def pop(self) -> int:
        ele = self.count_val[self.top].pop()
        self.val_count[ele] -= 1
        if not self.count_val[self.top]:
            self.top -= 1
        return ele
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()