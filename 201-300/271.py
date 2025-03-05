# https://neetcode.io/problems/string-encode-and-decode
# TIME: O(N)
# SPACE: O(N)
from typing import List
class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f'{s}\+' for s in strs)
    def decode(self, s: str) -> List[str]:
        res = s.split('\+')
        return [] if len(res) == 0 else res[:len(res)-1]
