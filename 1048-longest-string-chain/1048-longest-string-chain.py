class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        graph = defaultdict(set)
        words = set(words)
        for word in words:
            if len(word) > 1:
                for i in range(len(word)):
                    prev = word[:i] + word[i+1:]
                    if prev in words:
                        graph[prev].add(word)
        
        @lru_cache(None)
        def dfs(word):
            answer = 1
            for neigh in graph[word]:
                answer = max(answer, 1 + dfs(neigh))
            return answer
        
        res = 1
        for word in words:
            res = max(res, dfs(word))
        return res