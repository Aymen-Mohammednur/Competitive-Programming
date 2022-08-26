class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        r_cookie = len(s) - 1
        r_greed = len(g) - 1
        count = 0
        while r_cookie >= 0 and r_greed >= 0:
            if s[r_cookie] >= g[r_greed]:
                count += 1
                r_greed -= 1
                r_cookie -= 1
            else:
                r_greed -= 1
        return count