class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter = []
        digit = []
        for log in logs:
            if log.split()[1].isalpha():
                letter.append(log)
            else:
                digit.append(log)
        
        def comparator(log):
            letters = log.split()
            identifier, content = letters[0], letters[1:]
            return ' '.join(content) + ' ' + str(len(content)) + ' ' + identifier
        
        letter.sort(key=comparator)
        res = letter + digit
        return res