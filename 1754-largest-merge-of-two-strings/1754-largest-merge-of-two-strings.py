class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        # word1 = list(word1)
        # word2 = list(word2)
        merge = []
        word1P, word2P = 0, 0
        while word1P < len(word1) and word2P < len(word2):
            if word1[word1P:] > word2[word2P:]:
                merge.append(word1[word1P])
                word1P += 1
            else:
                merge.append(word2[word2P])
                word2P += 1
        return ''.join(merge) + word1[word1P:] + word2[word2P:]