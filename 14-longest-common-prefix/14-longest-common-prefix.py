class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # strs.sort(key=len)
        longest = strs[0]
        for i in range(1, len(strs)):
            count = 0
            for j in range(len(strs[i])):
                if j < len(longest) and strs[i][j] == longest[j]:
                    count += 1
                else:
                    break
            longest = longest[:count]
        return longest