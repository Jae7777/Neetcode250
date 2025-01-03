# https://neetcode.io/problems/task-scheduling
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        timeout = deque()
        pq = []
        counts = defaultdict(int)
        for task in tasks:
            counts[task] += 1
        for task in counts:
            pq.append((-counts[task], task))
        heapq.heapify(pq)
        cycles = 0
        while pq or timeout:
            if pq:
                task = heapq.heappop(pq)
                if task[0] < -1:
                    timeout.append((cycles, (task[0] + 1, task[1])))
            if timeout and cycles - timeout[0][0] >= n:
                heapq.heappush(pq, timeout.popleft()[1])
            cycles += 1
        return cycles