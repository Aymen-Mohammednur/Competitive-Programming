class Solution:
    def removePalindromeSub(self, s: str) -> int:
        def isPalindrome(s):
            left, right = 0, len(s) - 1
            while left <= right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        if isPalindrome(s):
            return 1
        else:
            return 2