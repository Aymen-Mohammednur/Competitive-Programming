class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return
        Set = set()
        result = set()
        for i in range(len(s) - 9):
            curr = s[i:10+i]
            if curr in Set:
                result.add(curr)
            else:
                Set.add(curr)
        return result