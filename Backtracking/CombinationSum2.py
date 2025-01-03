# https://neetcode.io/problems/combination-target-sum-ii
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        # [1, 2, 2, 4, 5, 6, 9]
        print(candidates)
        def createCombinations(start, currSum, currCombo):
            if currSum == target:
                res.append(currCombo)
                return
            i = start
            while i < len(candidates):
                num = candidates[i]
                if currSum + num > target:
                    break
                createCombinations(i + 1, currSum + num, currCombo + [num])
                while i + 1 < len(candidates) and num == candidates[i + 1]:
                    i += 1
                i += 1
    
        createCombinations(0, 0, [])
        return res
                
            