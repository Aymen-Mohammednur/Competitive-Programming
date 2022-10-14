class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        stack = []
        for course, pre in prerequisites:
            graph[pre].add(course)
        coloring = [0] * numCourses
        # hasCycle = False
        def dfs(pre):
            # nonlocal hasCycle
            # if hasCycle:
            #     return
            if coloring[pre] == 1:
                # hasCycle = True
                return False
            coloring[pre] = 1
            for course in graph[pre]:
                if coloring[course] != 2:
                    res = dfs(course)
                    if not res:
                        return
            stack.append(pre)
            coloring[pre] = 2
            return True
        for pre in range(numCourses):
            if coloring[pre] != 2:
                dfs(pre)
        stack.reverse()
        return stack if len(stack) == numCourses else []