# https://neetcode.io/problems/count-squares
# https://leetcode.com/problems/detect-squares/
from typing import List
from collections import defaultdict

class CountSquares:

    def __init__(self):
        self.xyCount = defaultdict(int)
        self.xy = []

    def add(self, point: List[int]) -> None:
        self.xyCount[(point[0], point[1])] += 1
        self.xy.append(point)

    def count(self, point: List[int]) -> int:
        squares = 0
        x_, y_ = point
        for x, y in self.xy:
            if (abs(x_ - x) != abs(y_ - y) or x_ == x or y_ == y):
                continue
            squares += self.xyCount[(x_, y)] * self.xyCount[(x, y_)]
        return squares
            