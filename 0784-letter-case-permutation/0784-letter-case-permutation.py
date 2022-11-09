class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        def backtrack(curr, index):
            if len(curr) == len(s):
                temp = "".join(curr.copy())
                ans.append(temp)
            for i in range(index, index + 1):
                if i < len(s):
                    if s[i].isnumeric():
                        curr.append(s[i])
                        backtrack(curr, index + 1)
                        curr.pop()
                    else:
                        curr.append(s[i].upper())
                        backtrack(curr, index + 1)
                        curr.pop()
                        curr.append(s[i].lower())
                        backtrack(curr, index + 1)
                        curr.pop()
        backtrack([], 0)
        return ans