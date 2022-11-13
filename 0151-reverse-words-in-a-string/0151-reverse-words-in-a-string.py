class Solution:
    def reverseWords(self, s: str) -> str:
        str_list = s.split(" ")
        res = []
        for i in range(len(str_list) - 1, -1, -1):
            if str_list[i] != '':
                res.append(str_list[i])
                res.append(' ')
        res.pop()
        return "".join(res)