class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        indegree = defaultdict(int)
        for a, b in prerequisites:
            graph[b].add(a)
            indegree[a] += 1
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        order = []
        while queue:
            curr = queue.popleft()
            order.append(curr)
            for neigh in graph[curr]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh)
        return order if len(order) == numCourses else []