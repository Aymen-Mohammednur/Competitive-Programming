class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = defaultdict(set)
        for i in range(len(strs)):
            sortedWord = ''.join(sorted(strs[i]))
            store[sortedWord].add(i)
        res = []
        for word in store:
            toAdd = []
            for indices in store[word]:
                toAdd.append(strs[indices])
            res.append(toAdd)
        return res