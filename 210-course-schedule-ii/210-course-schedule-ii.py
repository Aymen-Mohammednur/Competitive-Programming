class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        indegree = [0] * numCourses
        output = []
        for i, j in prerequisites:
            graph[j].add(i)
            indegree[i] += 1
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
            
        return output if len(output) == numCourses else []