class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = defaultdict(list)
        for i in range(len(strs)):
            sortedWord = ''.join(sorted(strs[i]))
            store[sortedWord].append(strs[i])
        res = []
        for word in store:
            res.append(store[word])
        return res