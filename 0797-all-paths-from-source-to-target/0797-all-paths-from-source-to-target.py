class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        def backtrack(curr, path):
            if curr == len(graph) - 1:
                paths.append(path.copy())
            for neigh in graph[curr]:
                path.append(neigh)
                backtrack(neigh, path)
                path.pop()
        backtrack(0, [0])
        return paths