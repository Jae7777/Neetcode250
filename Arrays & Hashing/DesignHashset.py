# https://leetcode.com/problems/design-hashset/
class MyHashSet:

    def __init__(self):
        self.numItems = 0
        self.buckets = [None] * 6

    def hash(self, key: int) -> None:
        return (key) % len(self.buckets)

    def resize(self, newSize: int) -> None:
        oldBuckets = self.buckets
        self.buckets = [None] * newSize
        for bucket in oldBuckets:
            if bucket:
                for item in bucket:
                    i = self.hash(item)
                    if not self.buckets[i]:
                        self.buckets[i] = []
                    self.buckets[i].append(item)

    def add(self, key: int) -> None:
        if self.numItems > int(len(self.buckets) * 1.3):
            self.resize(int(self.numItems * 1.3))
        i = self.hash(key)
        if not self.buckets[i]:
            self.buckets[i] = []
        if not self.contains(key):
            self.buckets[i].append(key)
            self.numItems += 1

    def remove(self, key: int) -> None:
        if self.numItems < int(len(self.buckets) * 0.7):
            self.resize(len(self.buckets))
        i = self.hash(key)
        if self.contains(key):
            self.buckets[i].remove(key)
            self.numItems -= 1

    def contains(self, key: int) -> bool:
        i = self.hash(key)
        if self.buckets[i] and key in self.buckets[i]:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)