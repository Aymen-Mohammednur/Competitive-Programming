class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(set)
        inDegree = defaultdict(int)
        for i in range(len(recipes)):
            for j in range(len(ingredients[i])):
                graph[ingredients[i][j]].add(recipes[i])
                if ingredients[i][j] not in supplies:
                    inDegree[recipes[i]] += 1
        queue = deque()
        for i in recipes:
            if inDegree[i] == 0:
                queue.append(i)
        result = []
        while queue:
            current = queue.popleft()
            result.append(current)
            for food in graph[current]:
                inDegree[food] -= 1
                if inDegree[food] == 0:
                    queue.append(food)
        return result