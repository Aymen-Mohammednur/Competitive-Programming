class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = defaultdict(int)
        graph = defaultdict(set)
        for course, pre in prerequisites:
            indegree[course] += 1
            graph[pre].add(course)
        queue = deque()
        for i in range(numCourses):
            if not indegree[i]:
                queue.append(i)
        res = []
        while queue:
            curr = queue.popleft()
            res.append(curr)
            for neigh in graph[curr]:
                indegree[neigh] -= 1
                if not indegree[neigh]:
                    queue.append(neigh)
        return res if len(res) == numCourses else []