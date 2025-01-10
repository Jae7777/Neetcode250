# https://neetcode.io/problems/gas-station
# mom can we have greedy?
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total = 0
        res = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                res = i + 1
        
        return res
# we already have greedy at home
# greedy at home:
class Solution: 
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        rightSum = [0] * len(gas)
        rightIndices = [-1] * len(gas)
        cumSum = [0] * len(gas)
        for i in range(len(gas)):
            g, c = gas[i], cost[i]
            if g - c > 0:
                rightSum[i] = g - c + (rightSum[i - 1] if i - 1 >= 0 and rightSum[i - 1] > 0 else 0)
                rightIndices[i] = rightIndices[i - 1] if i - 1 >= 0 and rightSum[i - 1] > 0 else i
            else:
                rightSum[i] = g - c + (rightSum[i - 1] if i - 1 >= 0 and rightSum[i - 1] < 0 else 0)
                rightIndices[i] = rightIndices[i - 1] if i - 1 >= 0 and rightSum[i - 1] < 0 else i
            cumSum[i] = g - c + (cumSum[i - 1] if i - 1 >= 0 else 0)

        if cumSum[-1] < 0:
            return -1
        for i in range(len(rightSum) - 1, -1, -1):
            if rightSum[i] >= 0:
                return rightIndices[i]
        return -1