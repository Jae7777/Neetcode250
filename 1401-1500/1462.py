# https://leetcode.com/problems/course-schedule-iv/
from collections import defaultdict
from typing import List
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(set)
        for u, v in prerequisites:
            graph[v].add(u)
    
        for course in list(graph.keys()): 
            visited = set()
            q = [course]
            while q:
                prereq = q.pop()
                if prereq in visited:
                    continue
                visited.add(prereq)
                for v in graph[prereq]: 
                    q.append(v)
            graph[course].update(visited)

        res = []
        for u, v in queries:
            res.append(u in graph[v])
        return res
