class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(set)
        indegree = defaultdict(int)
        for index, (a, b) in enumerate(prerequisites):
            indegree[a] += 1
            graph[b].add(a)
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        courses = []
        while queue:
            curr = queue.popleft()
            courses.append(curr)
            for neigh in graph[curr]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh)
        return len(courses) == numCourses