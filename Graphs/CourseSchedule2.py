# https://neetcode.io/problems/course-schedule-ii
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {course: [] for course in range(numCourses)}
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        visited = set()
        res = []
        def createOrder(course):
            if course not in graph:
                return True
            if course in visited:
                return False
            visited.add(course)
            for prereq in graph[course]:
                if not createOrder(prereq):
                    return False
            res.append(course)
            del graph[course]
            visited.remove(course)
            return True

        for course in list(graph):
            if not createOrder(course):
                return []
        return res