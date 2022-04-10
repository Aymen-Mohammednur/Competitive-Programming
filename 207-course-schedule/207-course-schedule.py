class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(set)
        indegree = [0] * numCourses
        output = []
        for course, pre in prerequisites:
            graph[pre].add(course)
            indegree[course] += 1
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        while queue:
            current = queue.popleft()
            output.append(current)
            for neighbors in graph[current]:
                indegree[neighbors] -= 1
                if indegree[neighbors] == 0:
                    queue.append(neighbors)
        return len(output) == numCourses