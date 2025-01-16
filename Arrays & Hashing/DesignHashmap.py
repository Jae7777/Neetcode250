# https://leetcode.com/problems/design-hashmap/
class MyHashMap:

    def __init__(self):
        self.buckets = [[] for _ in range(6)]
        self.size = 0

    def hash(self, key: int) -> int:
        return key % len(self.buckets)

    def resize(self, size: int) -> None:
        old_buckets = self.buckets
        self.buckets = [[] for _ in range(size)]
        for bucket in old_buckets:
            for item in bucket:
                i = self.hash(item[0])
                self.buckets[i].append((item[0], item[1]))

    def put(self, key: int, value: int) -> None:
        if self.size  > int(len(self.buckets) * 1.4):
            self.resize(int(len(self.buckets) * 1.4))
        i = self.hash(key)
        for j, item in enumerate(self.buckets[i]):
            if item[0] == key:
                self.buckets[i][j] = (key, value)
                return
        self.buckets[i].append((key, value))
        self.size += 1
        
    def get(self, key: int) -> int:
        i = self.hash(key)
        for k, v in self.buckets[i]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        if self.size < int(len(self.buckets) * 0.6):
            self.resize(int(len(self.buckets) * 0.6))
        i = self.hash(key)
        for j, item in enumerate(self.buckets[i]):
            if item[0] == key:
                self.buckets[i][j] = self.buckets[i][-1]
                self.buckets[i].pop()
                self.size -= 1
                return
    

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)