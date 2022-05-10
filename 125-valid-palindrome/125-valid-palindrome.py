class Solution:
    def isPalindrome(self, s: str) -> bool:
        phrase = ""
        for char in s:
            if char.isalpha():
                phrase += char.lower()
                continue
            if char.isalnum():
                phrase += char
        if not phrase:
            return True
        print(phrase)
        left = 0
        right = len(phrase) - 1
        while left <= right:
            if phrase[left] != phrase[right]:
                return False
            left += 1
            right -= 1
        return True