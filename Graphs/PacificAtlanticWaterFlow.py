# https://neetcode.io/problems/pacific-atlantic-water-flow
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(heights), len(heights[0])
        flowsPacific, flowsAtlantic = set(), set()
        res = []
        def waterFlowsInYou(flows, r, c, prevHeight):
            if r < 0 or c < 0 or r == ROW or c == COL or (r, c) in flows:
                return
            height = heights[r][c]
            if height < prevHeight:
                return
            flows.add((r, c))
            waterFlowsInYou(flows, r + 1, c, height)
            waterFlowsInYou(flows, r - 1, c, height)
            waterFlowsInYou(flows, r, c + 1, height)
            waterFlowsInYou(flows, r, c - 1, height)
        
        for r in range(ROW):
            waterFlowsInYou(flowsPacific, r, 0, float('-inf'))
            waterFlowsInYou(flowsAtlantic, r, COL - 1, float('-inf'))
        for c in range(COL):
            waterFlowsInYou(flowsPacific, 0, c, float('-inf'))
            waterFlowsInYou(flowsAtlantic, ROW - 1, c, float('-inf'))

        for r, c in (flowsPacific & flowsAtlantic):
            res.append([r, c])
        return res