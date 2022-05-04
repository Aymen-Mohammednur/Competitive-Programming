class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)
        output = ["z"] * 1000
        output = "".join(output)
        prev = None
        Max = 0
        words.sort()
        for word in words:
            if prev and word.startswith(prev):
                continue
            toSearch = word[:-1]
            if len(word) == 1:
                toSearch = word
            if trie.search(toSearch):
                if len(word) > Max:
                    Max = len(word)
                    output = word
                elif len(word) == Max:
                    output = min(output, word)
            else:
                prev = toSearch
        return "" if Max == 0 else output