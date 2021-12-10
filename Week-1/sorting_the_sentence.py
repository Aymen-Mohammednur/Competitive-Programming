def sortSentence(self, s: str) -> str:
    words = s.split(" ")
    for i in range(len(words)):
        minn = i
        for j in range(i + 1, len(words)):
            if (words[minn][-1] > words[j][-1]):
                minn = j
        words[i], words[minn] = words[minn], words[i]
    for i in range(len(words)):
        words[i] = words[i][:-1]
    
    return " ".join(words)