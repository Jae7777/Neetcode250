# https://leetcode.com/problems/greatest-common-divisor-traversal/description/
from typing import List

class DSU:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
        self.count = n
    def find(self, u):
        while u != self.par[u]:
            self.par[u] = self.par[self.par[u]]
            u = self.par[u]
        return u
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.rank[pu] > self.rank[pv]:
            self.rank[pu] += self.rank[pv]
            self.par[pv] = pu
        else:
            self.rank[pv] += self.rank[pu]
            self.par[pu] = pv
        self.count -= 1
        return True

class Solution:    
    def primeFactorization(self, num: int) -> List[int]:
        res = []
        limit = int(num ** 0.5)
        i = 2
        while i <= limit:
            if num % i == 0:
                res.append(i)
                while num % i == 0:
                    num //= i
                limit = int(num ** 0.5)
            i += 1
        if num != 1:
            res.append(num)
        return res

    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if nums.count(1) >= 1 and len(nums) >= 2:
            return False
        nums = list(set(nums))
        dsu = DSU(len(nums))
        graph = {}
        for i, num in enumerate(nums):
            factors = self.primeFactorization(num)
            for factor in factors:
                if factor in graph:
                    dsu.union(graph[factor], i)
                else:
                    graph[factor] = i
        cc = dsu.find(0)
        return True if all(cc == dsu.find(i) for i in range(1, len(nums))) else False