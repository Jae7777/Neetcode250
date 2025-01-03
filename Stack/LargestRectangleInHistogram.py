# https://neetcode.io/problems/largest-rectangle-in-histogram
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i, h in enumerate(heights):
            j = i
            while stack and stack[-1][0] > h:
                j = stack[-1][1]
                res = max(res, stack[-1][0] * (i - j))
                stack.pop()
            stack.append((h, j))
            stack.append((h, i))
        while stack:
            h, i = stack.pop()
            res = max(res, h * (len(heights) - i))
        return res