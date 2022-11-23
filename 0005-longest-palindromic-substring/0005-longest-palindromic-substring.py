class Solution:
    def palindromeSize(self, s, l, r):
        longest = [0, 0, 0]
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if longest[0] < r - l + 1:
                longest = [r - l + 1, l, r]
            l -= 1
            r += 1
        return longest
        
    def longestPalindrome(self, s: str) -> str:
        longest = [0, 0, 0]
        for i in range(len(s)):
            # for odd palindrome
            l, r = i, i
            pal = self.palindromeSize(s, l, r)
            if longest[0] < pal[0]:
                longest = pal
            
            # for even palindrome
            l, r = i, i + 1
            pal = self.palindromeSize(s, l, r)
            if longest[0] < pal[0]:
                longest = pal
        
        return s[longest[1]:longest[2] + 1]