class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c_counter = Counter(chars)
        ans = 0
        for word in words:
            good = True
            w_counter = Counter(word)
            for c in w_counter:
                if w_counter[c] > c_counter[c]:
                    good = False
                    break
            if good:
                ans += len(word)
        return ans