class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        curr = []
        visited = set()
        path = set()
        def dfs():
            if sum(curr) > n:
                return
            if sum(curr) >= n and len(curr) < k:
                return
            if len(curr) == k:
                if sum(curr) == n:
                    temp2 = sorted(curr)
                    temp = tuple(temp2)
                    if temp not in visited:
                        visited.add(temp)
                        result.append(temp2)
                return
            for i in range(1, 10):
                if i not in path:
                    curr.append(i)
                    path.add(i)
                    dfs()
                    curr.pop()
                    path.remove(i)
        dfs()
        return result