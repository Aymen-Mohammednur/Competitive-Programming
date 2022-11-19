class Solution:
    def isPalindrome(self, s: str) -> bool:
        actual_string = []
        for char in s:
            if char.isalnum():
                actual_string.append(char.lower())
        
        l, r = 0, len(actual_string) - 1
        while l <= r:
            if actual_string[l] != actual_string[r]:
                return False
            l += 1
            r -= 1
        return True