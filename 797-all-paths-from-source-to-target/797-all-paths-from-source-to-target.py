class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        def backtrack(curr, path, end):
            path.append(curr)
            if curr == end:
                paths.append(path.copy())
                return
            for neigh in graph[curr]:
                backtrack(neigh, path, end)
                path.pop()
        backtrack(0, [], len(graph) - 1)
        return paths