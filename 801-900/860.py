# https://leetcode.com/problems/lemonade-change/
from typing import List
# soo jank (beats 95.21% memory)
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count = { 5: 0, 10: 0, 20: 0 }
        for bill in bills:
            change = bill - 5
            if change == 0:
                count[5] += 1
            elif change == 5:
                if count[5] == 0:
                    return False
                count[change] -= 1
                count[bill] += 1
            elif change == 15:
                if (count[10] >= 1 and count[5] == 0) or (count[10] == 0 and count[5] < 3):
                    return False
                if count[10] > 0:
                    count[10] -= 1
                    count[5] -= 1
                else:
                    count[5] -= 3
                count[20] += 1
        return True

# cleaner (runs slower?)
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count = { 5: 0, 10: 0}
        for bill in bills:
            change = bill - 5
            if bill == 5:
                count[5] += 1
            elif bill == 10:
                if count[5] >= 1:
                    count[bill] += 1
                    count[change] -= 1
                else:
                    return False
            else:
                if count[10] >= 1 and count[5] >= 1:
                    count[10] -= 1
                    count[5] -= 1
                elif count[5] >= 3:
                    count[5] -= 3
                else:
                    return False
        return True