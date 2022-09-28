class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        def reverse(s, index):
            nonlocal i
            if index >= len(s):
                return
            reverse(s, index + 1)
            if i <= index:
                s[index], s[i] = s[i], s[index]
                i += 1
        
        reverse(s, 0)