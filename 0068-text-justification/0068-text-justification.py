class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = [] 
        curr = []
        letters = 0
        for word in words:
            if letters + len(word) + len(curr) > maxWidth:
                for i in range(maxWidth - letters):
                    curr[i%(len(curr)-1 or 1)] += ' '
                res.append(''.join(curr))
                curr, letters = [], 0
            curr += [word]
            letters += len(word)
        return res + [' '.join(curr).ljust(maxWidth)]