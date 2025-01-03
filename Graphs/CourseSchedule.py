# https://neetcode.io/problems/course-schedule
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        visited = set()
        def containsCycle(course):
            if course not in graph:
                return False
            if course in visited:
                return True
            visited.add(course)
            for prereq in graph[course]:
                if containsCycle(prereq):
                    return True
            del graph[course]
            visited.remove(course)
            return False

        for course in list(graph):
            if containsCycle(course):
                return False
        return True
    