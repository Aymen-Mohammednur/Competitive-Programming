class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capital = 0
        small = 0
        first = False
        for i in range(len(word)):
            char = word[i]
            if i == 0 and char.isupper():
                first = True
            if char.isupper():
                capital += 1
            else:
                small += 1
        return True if capital == len(word) or small == len(word) or (first and capital == 1) else False