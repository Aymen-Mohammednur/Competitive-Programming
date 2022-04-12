class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(set)
        inDegree = [0] * (n + 1)
        maxTime = -1
        for pre, course in relations:
            graph[pre].add(course)
            inDegree[course] += 1
        queue = Deque()
        for i in range(1, n + 1):
            if inDegree[i] == 0:
                queue.append(i)
        print(graph)
        endTime = defaultdict(int)
        maxTime = defaultdict(int)
        while queue:
            current = queue.popleft()
            endTime[current] = time[current - 1] + maxTime[current]
            for course in graph[current]:
                maxTime[course] = max(maxTime[course], endTime[current])
                inDegree[course] -= 1
                if inDegree[course] == 0:
                    queue.append(course)
        print(endTime)
        return max(endTime.values())