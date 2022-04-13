class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        paragraph = paragraph.split(' ')
        Dict = defaultdict(int)
        mostFreq = ''
        for index, word in enumerate(paragraph):
            word = word.lower()
            if not word.isalpha():
                while word and not word.isalpha():
                    word = word[:-1]
            if word.isalpha() and word not in banned:
                Dict[word] += 1
                if Dict[word] > Dict[mostFreq]:
                    mostFreq = word
        return mostFreq