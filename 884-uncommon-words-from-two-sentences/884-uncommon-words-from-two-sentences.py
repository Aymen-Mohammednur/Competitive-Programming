class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split(' ')
        s2 = s2.split(' ')
        Dict = defaultdict(int)
        for index, word in enumerate(s1):
            Dict[word] += 1
        for index, word in enumerate(s2):
            Dict[word] += 1
        result = []
        for word in Dict:
            if Dict[word] == 1:
                result.append(word)
        return result